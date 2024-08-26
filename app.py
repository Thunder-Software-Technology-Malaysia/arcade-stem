from flask import Flask, jsonify, request
import stripe

app = Flask(__name__)

# Set your Stripe secret key here (replace with your actual Stripe secret key)
stripe.api_key = 'sk_test_51Po2LG2MwOOp1GEXKimcGg9NMsMWnqsBlxSuWY1WbdcQ8qB6m24ectvUMN86vYn7mureqRUpc8UkHW29QIaSV5rn00ujWjiIuu'

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "up",
        "message": "API is running"
    })

@app.route('/payment_intent', methods=['POST'])
def create_payment_intent():
    try:
        # Extract the amount and currency from the request
        data = request.json
        amount = data.get('amount', 500)  # Default to $5.00 if not provided
        currency = data.get('currency', 'usd')

        # Create a PaymentIntent with the specified amount and currency
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card'],
        )

        # Return the client secret to the client
        return jsonify({
            "status": "success",
            "client_secret": intent.client_secret
        })
    except Exception as e:
        # Handle any errors that occur
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
