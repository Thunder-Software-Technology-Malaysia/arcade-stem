import os
import stripe
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import awsgi  # To wrap Flask in AWS Lambda

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set up the Stripe API key from environment variable
stripe.api_key = os.getenv("STRIPE_API_KEY")

if not stripe.api_key:
    raise ValueError("No STRIPE_API_KEY set for Flask application")

# Dictionary to track the status of machines
machine_status = {}

# Endpoint to create a payment link
@app.route('/create-payment-link', methods=['POST'])
def create_payment_link():
    try:
        data = request.json
        machine_id = data.get('machine_id')
        # Create a payment link with metadata for tracking the machine_id
        payment_link = stripe.PaymentLink.create(
            line_items=[{
                'price': 'price_1PuQrZ2MwOOp1GEXTkNAef1b',
                'quantity': 1,
            }],
            metadata={
                'machine_id': machine_id
            }
        )
        return jsonify({'url': payment_link.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Webhook to listen for payment events
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        return 'Invalid signature', 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        machine_id = session.get('metadata', {}).get('machine_id')
        amount_paid = session['amount_total']

        if machine_id:
            machine_status[machine_id] = {
                'status': 'paid',
                'amount': amount_paid,
                'timestamp': session['created'],
            }
            print(f"Payment for {machine_id} was successful!")
        else:
            print(f"Payment was successful but no machine_id was provided!")

    return '', 200

# AWS Lambda handler
def lambda_handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    app.run(port=5000)
