# Creating Stripe Webhooks

## Before You Start :clipboard:

### Prerequisites Checklist

Before setting up your webhook, you need:

* [x] Stripe account set up
* [ ] AWS Lambda function deployed with either:
    * Quick Deploy: Docker image pulled and deployed
    * Custom Build: Your code built and deployed
* [ ] API Gateway URL from AWS
* [ ] Environment variables configured in Lambda

!!! warning "Not Ready Yet?"
    If you haven't deployed your Lambda function:

    **Quick Deploy Path**

    1. [Pull the Docker Image](../../quick-deploy/docker-pull.md)
    2. [Deploy to AWS](../../quick-deploy/aws-config.md)
    3. Come back here!

    **Custom Build Path**

    1. [Build Your Code](../../custom-build/build-and-test.md)
    2. [Deploy to AWS](../../custom-build/first-deployment.md)
    3. Come back here!

!!! tip "Keep This Tab Open!"
    If you need to complete the prerequisites, bookmark this page - you'll need it after deploying your Lambda function!

# Creating Stripe Webhooks

## What are Webhooks? :incoming_envelope:

Think of webhooks as a "notification system" for your arcade cabinet. When someone makes a payment:

1. Stripe processes the payment
2. Stripe sends a message to your system
3. Your system adds credits to the cabinet

!!! tip "Real World Example"
    It's like when you order food delivery:

    * You pay on the app
    * The restaurant gets notified
    * They start making your food!

## Why Do We Need Webhooks? :thinking:

Webhooks are crucial for your arcade cabinet because they:

* Tell your system when a payment succeeds
* Help prevent cheating or errors
* Enable automatic credit adding
* Keep payment processing secure

## Setting Up Your Webhook :wrench:

### 1. Find Your API URL

First, you'll need your AWS API Gateway URL. It looks like:
```
https://abc123def.execute-api.us-west-2.amazonaws.com/prod
```

!!! note "Don't Have This Yet?"
    If you haven't set up AWS yet, bookmark this page and come back after completing the [AWS Setup](../aws-setup.md)!

### 2. Create the Webhook

1. In your Stripe Dashboard:

    * Go to "Developers" → "Webhooks"
    * Click "Add endpoint"

2. Configure Your Endpoint:

    * **URL**: Your API URL + `/addCredit`
    * **Description**: "Arcade Cabinet Payments"
    * Click "Select events"

3. Select Events:

    * Expand "Checkout"
    * Check `checkout.session.completed`
    * Click "Add events"

[!INSERT SCREENSHOT: Stripe webhook configuration page with fields highlighted]

### 3. Save Your Secret

After creating the webhook:

1. Look for "Signing secret"
2. Click "Reveal" 
3. Copy the secret (starts with `whsec_`)
4. Save it somewhere safe!

!!! danger "Keep This Secret!"
    Your webhook secret is like a password. Never:

    * Share it with anyone
    * Commit it to code
    * Post it online

## Testing Your Webhook :test_tube:

### 1. Install Stripe CLI

=== "Mac"
    ```bash
    brew install stripe/stripe-cli/stripe
    ```

=== "Windows"
    * Download from [Stripe CLI Releases](https://github.com/stripe/stripe-cli/releases)
    * Add to your system PATH

=== "Linux"
    ```bash
    # Download latest linux tar.gz from Stripe CLI releases
    sudo tar -xvf stripe_X.X.X_linux_x86_64.tar.gz -C /usr/local/bin
    ```

### 2. Test Locally

1. Login to Stripe:
   ```bash
   stripe login
   ```

2. Start webhook forwarding:
   ```bash
   stripe listen --forward-to localhost:5000/webhook
   ```

3. In a new terminal, send a test event:
   ```bash
   stripe trigger checkout.session.completed
   ```

### 3. Verify It Works

Look for these signs of success:

* Terminal shows "webhook received"
* Your system logs show the event
* Test credits appear correctly

## Common Issues :wrench:

### Webhook Not Working?

1. Check Your URL:

    * Is it spelled correctly?
    * Did you add `/addCredit` at the end?
    * Is your API Gateway running?

2. Verify Your Secret:

    * Is it set in your environment variables?
    * Did you copy it correctly?
    * Are you using the right secret for test/live mode?

3. Test Event Problems:

    * Are you selecting the right event type?
    * Is your system running when testing?
    * Can you see the events in Stripe dashboard?

!!! question "Still Stuck?"

    * Check our [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Look at your Lambda logs
    * Review Stripe's webhook logs

## Going Live :rocket:

Before accepting real payments:

1. Update webhook URL:

    * Change from localhost to your production URL
    * Add new webhook endpoint for live mode
    * Get new webhook secret for live mode

2. Set up monitoring:

    * Enable webhook monitoring
    * Set up failure notifications
    * Test with real test payments

## Next Steps :arrow_forward:

Now that your webhook is set up:

1. Save your webhook secret
2. Update your environment variables
3. Test the complete payment flow
4. Monitor for successful operation

[Continue to Testing →](../../quick-deploy/testing.md){ .md-button .md-button--primary }
[Back to Stripe Setup](stripe-setup.md){ .md-button }