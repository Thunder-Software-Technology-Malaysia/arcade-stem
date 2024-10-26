# Setting Up Your EMQX Account

Welcome to your first setup step! Before we configure AWS or Stripe, we'll set up EMQX - the messaging system that will help your arcade cabinet communicate. Think of it like a super-fast mail service for your arcade! :mailbox_with_mail:

## What is EMQX? :thinking:

EMQX is a messaging system that will:

* Send messages when someone pays
* Tell games when to start
* Signal when games are over
* Handle all communication securely

!!! info "Why Start with EMQX?"
    We're setting up EMQX first because:
    
    * It's the quickest to set up
    * We'll need it to test other components
    * It helps you understand how the parts connect
    * The free tier is perfect for learning

## Before You Start :clipboard:

You'll need:

* An email address
* About 10-15 minutes
* A way to save important information

!!! tip "Keep Notes"
    Create a document to save these important details:

    * Broker URL
    * Port numbers
    * Username
    * Password

## Setting Up Your Account :key:

### 1. Create Your Account

1. Visit [https://accounts.emqx.com/signup](https://accounts.emqx.com/signup)
2. Enter your email address
3. Create a strong password
4. Verify your email

### 2. Create a Deployment

1. Log into EMQX Cloud Console
2. Click "Create Deployment"
3. Choose "Serverless" (Free tier)
4. Pick a name (like "ArcadeMessenger")

!!! success "Free Tier Perfect for Learning"
    You get plenty for your arcade system:

    * 1 million messages per month
    * 1 GB traffic per month
    * Multiple cabinet support
    * No credit card required!

## Essential Configuration :gear:

### 1. Get Your Connection Details

After deployment is ready:

1. Save your **Broker URL**
2. Note these **Port Numbers**:

   * 8883 - For secure MQTT (we'll use this one)
   * 1883 - For standard MQTT
   * 8083 - For WebSocket

### 2. Set Up Authentication

1. Go to "Authentication" in sidebar
2. Click "Create"
3. Create and save:

   * Username (like "arcade-user")
   * Strong password

!!! danger "Keep These Safe!"
    Save your credentials securely - you'll need them for AWS setup next!

## Quick Test :test_tube:

Let's make sure everything works! We'll use the Mosquitto CLI tool:

=== "Windows"
    ```bash
    # Install from: https://mosquitto.org/download/
    
    # Test subscribing to arcade topics
    mosquitto_sub -h your-broker.emqx.cloud -p 8883 ^
      -t "arcade/machine/+/coinpulse" ^
      --cafile emqx.crt ^
      -u "your-username" -P "your-password"
    ```

=== "Mac"
    ```bash
    # Install Mosquitto
    brew install mosquitto
    
    # Test subscribing to arcade topics
    mosquitto_sub -h your-broker.emqx.cloud -p 8883 \
      -t "arcade/machine/+/coinpulse" \
      --cafile emqx.crt \
      -u "your-username" -P "your-password"
    ```

=== "Linux"
    ```bash
    # Install Mosquitto
    sudo apt-get install mosquitto-clients
    
    # Test subscribing to arcade topics
    mosquitto_sub -h your-broker.emqx.cloud -p 8883 \
      -t "arcade/machine/+/coinpulse" \
      --cafile emqx.crt \
      -u "your-username" -P "your-password"
    ```

!!! tip "Don't worry if this test doesn't work yet!"
    We still need to set up security certificates. We'll do that during AWS setup.

## Understanding the Free Tier :moneybag:

Your free account includes:

* 1 million session minutes/month
* 1 GB traffic/month
* Messages up to 1 MB each
* 1000 message queue length
* 2-hour inactive session timeout

!!! success "Perfect for Learning"
    These limits are way more than enough for:

    * Learning the system
    * Testing your cabinet
    * Initial deployment

## What You've Accomplished :trophy:

You've now got:

1. ✅ An EMQX Cloud account
2. ✅ A serverless deployment
3. ✅ Your broker URL and ports
4. ✅ Authentication credentials

## Next Steps :arrow_forward:

Now that your messaging system is ready:

1. Keep your credentials handy
2. Double-check your broker URL
3. Get ready to set up AWS!

[Continue to AWS Setup →](../aws/basic-setup){ .md-button .md-button--primary }

## Quick Troubleshooting :wrench:

Having issues?

### Can't Create Account
* Check your email for verification
* Try a different browser
* Clear browser cache

### Deployment Failed
* Make sure you selected "Serverless"
* Try a different region
* Check your email is verified

!!! question "Need Help?"
    * Ask your teacher or mentor
    * Check our [Troubleshooting Guide](../troubleshooting/common-issues.md)
    * Visit [EMQX Docs](https://docs.emqx.com)