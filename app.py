import os
import stripe
import paho.mqtt.client as mqtt
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import awsgi
import datetime
import json
import ssl

# Load environment variables
load_dotenv()

app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_API_KEY")

if not stripe.api_key:
    raise ValueError("No STRIPE_API_KEY set for Flask application")

# MQTT settings
MQTT_BROKER = 'g38a1ef7.ala.asia-southeast1.emqxsl.com'  # EMQX Cloud broker address
MQTT_PORT = 8883  # SSL/TLS port
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CA_CERT_PATH = os.path.join(BASE_DIR, 'ca.crt')

# Initialize Paho MQTT Client
client = mqtt.Client()

# Add username and password for MQTT authentication
client.username_pw_set(username=os.getenv("MQTT_USERNAME"), password=os.getenv("MQTT_PASSWORD"))

# Callback function to check if connected successfully
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect to MQTT Broker. Return code: {rc}")

# Callback function for when connection is lost
def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")

# Configure TLS for encrypted connection
client.tls_set(
    ca_certs=CA_CERT_PATH,
    certfile=None,
    keyfile=None,
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# Set connection callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to the MQTT broker
try:
    client.connect(MQTT_BROKER, MQTT_PORT)
    print(f"Attempting to connect to MQTT broker at {MQTT_BROKER}:{MQTT_PORT} with SSL.")
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Start the MQTT loop in a separate thread
client.loop_start()

# Dictionary to track machine statuses
machine_status = {}

# Utility function to get the current timestamp in the required format
def get_timestamp():
    return datetime.datetime.utcnow().isoformat() + 'Z'  # ISO 8601 format

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

        # Create a payment link via Stripe API
        payment_link = stripe.PaymentLink.create(
            line_items=[{
                'price': 'price_1PuQrZ2MwOOp1GEXTkNAef1b',  # Replace with your actual Stripe price ID
                'quantity': 1,
            }],
            metadata={'machine_id': machine_id}  # Store machine_id in metadata
        )

        # Manually append the client_reference_id to the generated payment link
        payment_url_with_id = f"{payment_link.url}?client_reference_id={machine_id}"

        # Return the payment link with the client_reference_id attached
        return jsonify({'url': payment_url_with_id})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/addCredit', methods=['POST'])
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

    # Handle checkout session completion
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

            # Publish Coin Pulse Signal to MQTT
            coin_pulse_signal = {
                "machineId": machine_id,
                "credits": amount_paid // 100,  # Assuming each credit is worth 100 cents
                "timestamp": get_timestamp()
            }
            coin_pulse_message = json.dumps(coin_pulse_signal)
            print(f"Publishing Coin Pulse Signal: {coin_pulse_signal}")
            result = client.publish(f"arcade/machine/{machine_id}/coinpulse", coin_pulse_message)
            print(f"MQTT publish result: {result.rc}")  # Log the result code

    return '', 200

@app.route('/gameover', methods=['POST'])
def game_over():
    try:
        data = request.json
        machine_id = data.get('machine_id')
        print(f"Received game over signal for machine ID: {machine_id}")

        if machine_id in machine_status:
            # Publish Game Over Signal to MQTT
            game_over_signal = {
                "machineId": machine_id,
                "status": "game_over",
                "timestamp": get_timestamp()
            }
            game_over_message = json.dumps(game_over_signal)  # Convert signal to JSON
            print(f"Publishing Game Over Signal: {game_over_message}")

            # Publish the message and check the result
            result = client.publish(f"arcade/machine/{machine_id}/gameover", game_over_message)
            print(f"MQTT publish result: {result.rc}")  # Log the result code

            # Reset machine status to allow new payments
            del machine_status[machine_id]
            print(f"Machine {machine_id} status reset")

        return jsonify({"message": "Game over signal sent"}), 200
    except Exception as e:
        print(f"Error in game over process: {str(e)}")
        return jsonify({'error': str(e)}), 500

def lambda_handler(event, context):
    # AWS Lambda handler
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
