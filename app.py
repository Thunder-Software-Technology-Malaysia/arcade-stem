import os
import stripe
import paho.mqtt.client as mqtt
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import awsgi

# Load environment variables
load_dotenv()

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_API_KEY")

# MQTT settings
MQTT_BROKER = 'test.mosquitto.org'  # Use your broker here if running a local Mosquitto instance
MQTT_PORT = 1883

# Initialize MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

# Dictionary to track machine statuses
machine_status = {}

@app.route('/status', methods=['GET'])
def status():
    print("Status endpoint called")
    return jsonify({
        "status": "up",
        "message": "API is running"
    })

@app.route('/create-payment-link', methods=['POST'])
def create_payment_link():
    try:
        data = request.json
        machine_id = data.get('machine_id')
        print(f"Received request to create payment link for machine ID: {machine_id}")

        payment_link = stripe.PaymentLink.create(
            line_items=[{
                'price': 'price_1PuQrZ2MwOOp1GEXTkNAef1b',
                'quantity': 1,
            }],
            metadata={'machine_id': machine_id}
        )
        print(f"Payment link created: {payment_link.url}")
        return jsonify({'url': payment_link.url})
    except Exception as e:
        print(f"Error in creating payment link: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    print(f"Received Stripe webhook with payload: {payload}")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
        print(f"Webhook verified, event type: {event['type']}")
    except ValueError:
        print("Invalid payload")
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError:
        print("Invalid signature")
        return 'Invalid signature', 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        machine_id = session.get('metadata', {}).get('machine_id')
        amount_paid = session['amount_total']
        print(f"Checkout session completed for machine {machine_id}, amount paid: {amount_paid}")

        if machine_id:
            # Update machine status
            machine_status[machine_id] = {
                'status': 'paid',
                'amount': amount_paid,
                'timestamp': session['created'],
            }
            # Publish status to MQTT topic
            mqtt_message = f"Machine {machine_id} status updated: {machine_status[machine_id]}"
            print(f"Publishing MQTT message: {mqtt_message}")
            client.publish(f"arcade/machine/{machine_id}/status", mqtt_message)

    return '', 200

def lambda_handler(event, context):
    print(f"Lambda function invoked with event: {event}")
    return awsgi.response(app, event, context)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
