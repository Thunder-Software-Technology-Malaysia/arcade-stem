# Common Issues

Welcome to the troubleshooting guide! Having problems? Don't worry - we'll help you fix them! :wrench:

## How to Use This Guide :books:

1. Find your issue category (AWS, Stripe, etc.)
2. Look for your specific problem
3. Try the solutions in order
4. If still stuck, check "Getting More Help"

!!! tip "Before You Start"
    Always check these basics first:

    * Are you connected to the internet?
    * Did you save all your changes?
    * Are your environment variables set?
    * Is your virtual environment activated?

## AWS Issues :cloud:

### Lambda Function Not Deploying

**Symptoms:**

* Error when trying to deploy to Lambda
* Deployment seems stuck
* Function shows as failed

**Solutions:**

1. Check Image Architecture
    ```bash
    # If using M1/M2/M3 Mac, build with platform flag:
    docker buildx build --platform linux/amd64 --no-cache -t arcade-game-app .
    ```

2. Verify IAM Permissions
    * Go to IAM in AWS Console
    * Check user permissions
    * Ensure Lambda execution role exists
    * Verify API Gateway permissions

3. Check Function Configuration
    * Memory should be at least 128MB
    * Timeout should be 30 seconds
    * Handler should match your code

### API Gateway Not Working

**Symptoms:**
* 403 Forbidden errors
* Can't reach your API endpoints
* Integration timeout errors

**Solutions:**

1. Check CORS Settings
    * Verify CORS is enabled
    * Check allowed methods
    * Verify allowed headers

2. Check Route Configuration
    * Verify route paths match exactly
    * Check integration settings
    * Ensure deployment stage is set

3. Test Local vs. Production
    ```bash
    # Test locally first
    curl http://localhost:5000/status

    # Then test production
    curl https://your-api-id.execute-api.region.amazonaws.com/prod/status
    ```

### Free Tier Concerns

**Symptoms:**

* Unexpected charges
* Usage warnings
* Service limitations

**Solutions:**

1. Set Up Billing Alerts

    * Go to AWS Billing Dashboard
    * Create billing alert
    * Set threshold below limits

2. Monitor Usage

    * Check Lambda invocations
    * Monitor API Gateway calls
    * Review CloudWatch logs

## Stripe Issues :credit_card:

### Payment Link Not Working

**Symptoms:**

* QR code doesn't load
* Payment page error
* Invalid URL errors

**Solutions:**

1. Verify API Key
    ```python
    # Check which API key you're using
    print(stripe.api_key.startswith('sk_test_'))  # Should be True in test mode
    ```

2. Check Price ID
    * Verify price exists in Stripe
    * Confirm correct mode (test/live)
    * Check price is active

3. Test Creating Link
    ```bash
    curl -X POST http://localhost:5000/create-payment-link \
      -H "Content-Type: application/json" \
      -d '{"machine_id":"test123"}'
    ```

### Webhook Not Receiving Events

**Symptoms:**
* Payments succeed but no credits added
* No webhook logs in Stripe
* API not receiving notifications

**Solutions:**

1. Check Webhook Configuration
    * Verify endpoint URL
    * Check webhook secret
    * Confirm selected events

2. Test Locally with Stripe CLI
    ```bash
    # Start webhook forwarding
    stripe listen --forward-to localhost:5000/webhook

    # Test webhook
    stripe trigger checkout.session.completed
    ```

3. Check API Logs
    * Look for webhook requests
    * Check for signature errors
    * Verify payload processing

## MQTT Issues :satellite:

### Connection Problems

**Symptoms:**

* Can't connect to MQTT broker
* Connection drops frequently
* SSL/TLS errors

**Solutions:**

1. Check Credentials
    ```bash
    # Test connection with mosquitto_sub
    mosquitto_sub -h your.emqx.broker -p 8883 \
      -t "arcade/machine/+/coinpulse" \
      --cafile emqx.ca \
      -u "your_username" -P "your_password"
    ```

2. Verify SSL/TLS Setup
    * Check certificate file exists
    * Verify certificate isn't expired
    * Confirm correct file path

3. Test Network
    * Check firewall settings
    * Verify port 8883 is open
    * Test broker connection

### Messages Not Received

**Symptoms:**

* Cabinet not getting coin pulse
* Game over signals lost
* Delayed message delivery

**Solutions:**

1. Check Topic Subscription
    * Verify topic patterns
    * Check machine ID format
    * Confirm subscription active

2. Monitor Message Flow
    * Use EMQX dashboard
    * Check message delivery
    * Verify QoS levels

## Game Control Issues :video_game:

### Credits Not Adding

**Symptoms:**

* Payment successful but no credits
* Game won't start
* Credit display incorrect

**Solutions:**

1. Check MQTT Messages
    ```bash
    # Monitor coin pulse messages
    mosquitto_sub -h your.emqx.broker -p 8883 \
      -t "arcade/machine/+/coinpulse" \
      --cafile emqx.ca \
      -u "your_username" -P "your_password"
    ```

2. Verify Machine ID
    * Check payment metadata
    * Confirm correct ID format
    * Test with known working ID

3. Monitor State Changes
    * Check credit counter
    * Verify game state
    * Look for error messages

### Game Won't Start

**Symptoms:**

* Credits added but game inactive
    * Stuck on attract screen
    * Controls not responding
    * System unresponsive

**Solutions:**

1. Check Game State
    * Verify current mode
    * Check credit count
    * Monitor MQTT messages

2. Test Controls
    * Verify USB connections
    * Check control mapping
    * Test basic input

## Development Issues :computer:

### Docker Build Problems

**Symptoms:**

* Build fails
* Missing dependencies
* Architecture mismatch

**Solutions:**

1. Check Platform Settings
    ```bash
    # For M1/M2/M3 Macs
    docker buildx build --platform linux/amd64 --no-cache -t arcade-game-app .

    # View image details
    docker inspect arcade-game-app
    ```

2. Verify Dependencies
    * Check requirements.txt
    * Verify Python version
    * Confirm all imports

### Environment Setup Issues

**Symptoms:**

* Missing variables
* Import errors
* Configuration problems

**Solutions:**

1. Check Virtual Environment
    ```bash
    # Create new environment if needed
    python -m venv venv

    # Activate environment
    source venv/bin/activate  # Unix
    .\venv\Scripts\activate   # Windows
    ```

2. Verify Environment Variables
    ```bash
    # Check if variables are set
    python
    >>> import os
    >>> print(os.getenv('STRIPE_API_KEY'))
    ```

## Getting More Help :sos:

If you're still stuck:

1. Check Error Messages
    * Read the full error text
    * Look for specific codes
    * Check related logs

2. Gather Information
    * Which step failed?
    * What changed recently?
    * What are the exact errors?

3. Get Help
    * Ask your teacher/mentor
    * Check service documentation
    * Search error messages

!!! question "Still Need Help?"
    * Describe the problem clearly
    * Share relevant error messages
    * Explain what you've tried
    * Provide system details

## Quick Reference :bookmark_tabs:

### Common Terminal Commands

```bash
# Check Python version
python --version

# Check Docker version
docker --version

# Test API endpoint
curl http://localhost:5000/status

# Monitor MQTT messages
mosquitto_sub -h broker -p 8883 -t "arcade/machine/+/coinpulse"
```

### Useful Links

* [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/)
* [Stripe API Docs](https://stripe.com/docs/api)
* [EMQX Docs](https://docs.emqx.io/)
* [Getting Help Guide](getting-help.md)

Remember: Most problems have simple solutions. Take your time, check the basics, and don't hesitate to ask for help! :star: