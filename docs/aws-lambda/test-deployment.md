# Testing Your Deployment

Now that your API is deployed, let's make sure everything works! We'll test each part of your system step by step. :microscope:

## Prerequisites ✅

Before starting, make sure you have:

* Your API Gateway URL (from previous step)
* Stripe CLI installed
* MQTT client (Mosquitto) installed
* Test environment variables configured in Lambda

!!! tip "Keep Your Tools Ready"
    You'll need several terminal windows open for testing. Consider using VSCode's integrated terminal with split panes to keep everything organized!

## Part 1: Basic API Testing 🔍

Let's start by making sure your API endpoints are accessible.

### 1. Test Status Endpoint

```bash
curl https://your-api-url/status
```

Expected response:
```json
{
    "status": "up",
    "message": "API is running"
}
```

!!! warning "Getting a 404?"
    If you get a "Not Found" error:

    * Double-check your API URL
    * Verify the endpoint is deployed
    * Check Lambda logs for errors

## Part 2: Payment Flow Testing 💳

### 1. Create Payment Link

```bash
curl -X POST https://your-api-url/create-payment-link \
  -H "Content-Type: application/json" \
  -d '{"machine_id":"test123"}'
```

Expected response:
```json
{
    "url": "https://checkout.stripe.com/c/pay/cs_test_..."
}
```

### 2. Test Payment Processing

1. Start Stripe webhook forwarding:
```bash
stripe listen --forward-to https://your-api-url/addCredit
```

2. Open the payment URL in your browser

3. Complete a test payment:

    * Card number: 4242 4242 4242 4242
    * Any future expiry date
    * Any 3-digit CVC
    * Any ZIP code

!!! tip "Test Cards"
    Stripe provides several test cards for different scenarios:

    * 4242 4242 4242 4242 - Successful payment
    * 4000 0000 0000 9995 - Declined payment
    * Find more in the [Stripe testing docs](https://stripe.com/docs/testing)

## Part 3: MQTT Message Testing 📡

### 1. Watch for Messages

In a new terminal, subscribe to MQTT topics:

```bash
mosquitto_sub -h your.emqx.cloud.broker -p 8883 \
  -t "arcade/machine/+/coinpulse" \
  -t "arcade/machine/+/gameover" \
  --cafile emqx.ca \
  -u "your_username" -P "your_password"
```

### 2. Test Game Over Signal

```bash
curl -X POST https://your-api-url/gameover \
  -H "Content-Type: application/json" \
  -d '{"machine_id":"test123"}'
```

Watch your MQTT subscriber terminal for the game over message!

## Part 4: End-to-End Testing 🔄

Time to test the complete flow! You should see:

1. Payment link creation ✓
2. Successful payment ✓
3. MQTT coin pulse message ✓
4. Game over signal ✓
5. MQTT game over message ✓

!!! success "Working System"
    If you see all these steps working, congratulations! Your arcade payment system is ready for action! 🎮

## Monitoring and Logs 📊

### Check CloudWatch Logs

1. Go to AWS Console → CloudWatch → Log Groups
2. Find your Lambda function's log group
3. Look for any errors or warnings

### Monitor Stripe Dashboard

1. Go to Stripe Dashboard → Events
2. Look for successful test payments
3. Verify webhook deliveries

!!! tip "Log Investigation"
    If something's not working, logs are your best friend! They'll tell you exactly where things went wrong.

## Common Issues and Solutions 🔧

### API Gateway Issues

* **403 Forbidden**: Check Lambda permissions
* **502 Bad Gateway**: Review Lambda function configuration
* **Timeout**: Adjust Lambda timeout settings

### Stripe Issues

* **Webhook errors**: Verify endpoint URL and secrets
* **Payment failures**: Check test card numbers
* **Missing events**: Confirm webhook forwarding is running

### MQTT Issues

* **Connection refused**: Check broker address and credentials
* **No messages**: Verify topic subscriptions
* **SSL errors**: Check certificate configuration

!!! question "Still Stuck?"
    * Check the [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Review specific error messages
    * Ask your teacher or mentor for help

## Security Checks 🔐

Before finishing testing, verify:

1. Environment variables are properly set
2. Stripe webhook secret is configured
3. MQTT credentials are secure
4. API endpoints are working as expected

## Next Steps 🎯

Once testing is complete:

1. Document any issues found
2. Save test outputs for reference
3. Plan your next features or modifications
4. Consider moving to production mode

[Continue to Making Modifications →](../custom-build/modifications.md){ .md-button .md-button--primary }
[Back to API Gateway Setup](setup-gateway.md){ .md-button }

!!! tip "Keep Testing!"
    Regular testing helps catch issues early. Consider setting up automated tests for your system!