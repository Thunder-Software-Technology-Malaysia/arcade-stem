# API Reference

Welcome to the Artcade API documentation! This guide explains all the ways your code can talk to the arcade system. Let's make it fun! 🎮

## API Overview 🌐

Your arcade API has four main endpoints:

* Check if everything's working (`/status`)
* Create payment QR codes (`/create-payment-link`)
* Process payments (`/addCredit`)
* Handle game endings (`/gameover`)

!!! tip "Think of it Like a Restaurant"
    * `/status` is like checking if the restaurant is open
    * `/create-payment-link` is like creating a menu QR code
    * `/addCredit` is like processing a payment at the register
    * `/gameover` is like clearing a table for the next customer

## Base URL 🔗

Your API will be available at:
```
https://your-api-id.execute-api.your-region.amazonaws.com/prod
```

!!! note "Finding Your URL"
    You'll get your specific URL when you set up API Gateway in AWS. It will look similar to:
    ```
    https://abc123def.execute-api.us-west-2.amazonaws.com/prod
    ```

## Endpoints 🎯

### Check Status

Checks if your API is running properly.

```http
GET /status
```

#### Response

```json
{
    "status": "up",
    "message": "API is running"
}
```

!!! example "Testing Status"
    ```bash
    curl https://your-api-url/status
    ```

### Create Payment Link

Creates a QR code payment link for your arcade cabinet.

```http
POST /create-payment-link
```

#### Request Body

```json
{
    "machine_id": "your-machine-id",
    "price_id": "price_xxxxxxxxxxxxx",  // Optional
    "quantity": 1                       // Optional
}
```

#### Parameters

* `machine_id` (required): Your unique arcade cabinet ID
* `price_id` (optional): Stripe price ID for custom pricing
* `quantity` (optional): Number of credits to purchase

#### Response

```json
{
    "url": "https://checkout.stripe.com/..."
}
```

!!! example "Creating a Payment Link"
    ```bash
    curl -X POST https://your-api-url/create-payment-link \
      -H "Content-Type: application/json" \
      -d '{"machine_id":"arcade123"}'
    ```

### Process Payment

Handles Stripe webhook notifications when a payment succeeds.

```http
POST /addCredit
```

!!! warning "Webhook Security"
    This endpoint is called by Stripe with a special signature. Don't call it directly!

#### Headers

* `Stripe-Signature`: Special code from Stripe to verify the webhook

#### Webhook Event

```json
{
    "type": "checkout.session.completed",
    "data": {
        "object": {
            "metadata": {
                "machine_id": "arcade123"
            },
            "amount_total": 100
        }
    }
}
```

#### Response

* `200 OK`: Payment processed successfully
* `400 Bad Request`: Invalid webhook
* `500 Error`: Processing failed

### Game Over

Signals that a game has ended.

```http
POST /gameover
```

#### Request Body

```json
{
    "machine_id": "arcade123"
}
```

#### Response

```json
{
    "message": "Game over signal sent"
}
```

!!! example "Sending Game Over"
    ```bash
    curl -X POST https://your-api-url/gameover \
      -H "Content-Type: application/json" \
      -d '{"machine_id":"arcade123"}'
    ```

## MQTT Messages 📨

Your API publishes these MQTT messages:

### Coin Pulse Signal

Sent when credits should be added:

```json
{
    "machineId": "arcade123",
    "credits": 1,
    "timestamp": "2024-07-01T12:00:00Z"
}
```

### Game Over Signal

Sent when a game ends:

```json
{
    "machineId": "arcade123",
    "status": "game_over",
    "timestamp": "2024-07-01T12:30:00Z"
}
```

## Testing Tips 🧪

### Test Cards

Use these Stripe test cards:

* Success: `4242 4242 4242 4242`
* Decline: `4000 0000 0000 0002`
* Error: `4000 0000 0000 9995`

!!! tip "Test Card Details"
    * Use any future expiry date
    * Any 3-digit CVC
    * Any 5-digit ZIP code

### Using Stripe CLI

Test webhooks locally:

1. Start webhook forwarding:
   ```bash
   stripe listen --forward-to localhost:5000/webhook
   ```

2. Trigger test events:
   ```bash
   stripe trigger checkout.session.completed
   ```

## Error Handling 🔧

Your API returns standard HTTP status codes:

* `200`: Everything worked
* `400`: Something wrong with the request
* `401`: Not authorized
* `404`: Endpoint not found
* `500`: Server error

Error responses look like:
```json
{
    "error": "Description of what went wrong"
}
```

## Rate Limits 📊

Free tier limits:

* AWS Lambda: 1,000,000 requests/month
* EMQX: 1 GB traffic/month
* Stripe: No monthly limits

!!! warning "Stay Within Limits"
    * Monitor your usage in AWS Console
    * Watch EMQX dashboard
    * Check Stripe dashboard

## Security Best Practices 🔐

1. Never share:
    * API keys
    * Webhook secrets
    * MQTT credentials
    * AWS credentials

2. Always use:
    * HTTPS endpoints
    * Webhook signatures
    * SSL/TLS for MQTT
    * Environment variables

## Need Help? 🤔

If you run into problems:

1. Check the logs:
    * AWS CloudWatch
    * EMQX Dashboard
    * Stripe Dashboard

2. Common issues:
    * Wrong API URL
    * Invalid credentials
    * Network problems
    * Rate limiting

!!! question "Still Stuck?"
    * Check our [Troubleshooting Guide](../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Review error messages
    * Try test endpoints first

## Next Steps 🚀

Now that you understand the API:

1. Test the status endpoint
2. Create a test payment
3. Monitor the results
4. Try the game over signal

[Try Quick Deploy →](../quick-deploy/overview.md){ .md-button .md-button--primary }
[Custom Build Guide →](../custom-build/overview.md){ .md-button }