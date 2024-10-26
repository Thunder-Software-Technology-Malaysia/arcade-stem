# Building and Testing Your System 🛠️

Now that you understand how the code works, let's get it running on your computer and test everything! We'll build and test locally first, then handle containerization and deployment in the next section.

## Prerequisites ✅

Before starting, make sure you have:

* All accounts set up ([AWS](../accounts/aws.md), [Stripe](../accounts/stripe.md), [EMQX](../accounts/emqx.md))
* Python 3.9 or higher installed
* Visual Studio Code (VSCode) installed
* Git installed
* Your code cloned from GitHub

!!! tip "Quick Check"
    Run these commands in your terminal to verify your setup:
    ```bash
    python --version  # Should show 3.9 or higher
    git --version    # Should show Git version
    ```

## Part 1: Setting Up Your Development Environment 💻

### 1. Create Your Environment File

1. In your project folder, create a new file called `.env.local`:
   ```bash
   # In VSCode, right-click in the explorer and select "New File"
   # Name it .env.local
   ```

2. Add your configuration (replace with your actual values):
   ```ini
   STRIPE_API_KEY=sk_test_your_stripe_key
   STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
   STRIPE_PRICE_ID=price_your_price_id
   MQTT_USERNAME=your_mqtt_username
   MQTT_PASSWORD=your_mqtt_password
   MQTT_BROKER=your.emqx.cloud.broker
   MQTT_PORT=8883
   ```

!!! warning "Keep It Secret!"
    Never commit your `.env.local` file to Git! It should already be in `.gitignore`.

### 2. Set Up Your Python Virtual Environment

Create and activate a virtual environment (open termninal in vs code):

=== "Windows"
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

=== "Mac/Linux"
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Part 2: Testing Your System 🧪

Let's test each component to make sure everything works!

### 1. Test Local API 

1. Start the Flask application (you paste this into terminal and run the command):
   ```bash
   python app.py
   ```

2. In a new terminal, test the status endpoint:
   ```bash
   curl http://localhost:5000/status
   ```

   You should see:
   ```json
   {
     "status": "up",
     "message": "API is running"
   }
   ```

### 2. Test MQTT Connection 📡

1. Install the Mosquitto MQTT client:

=== "Windows"
    Download from: https://mosquitto.org/download/
    
=== "Mac"
    ```bash
    brew install mosquitto
    ```

=== "Linux"
    ```bash
    sudo apt-get install mosquitto-clients
    ```

2. Subscribe to test messages:
   ```bash
   mosquitto_sub -h your.emqx.cloud.broker -p 8883 \
     -t "arcade/machine/+/coinpulse" \
     -t "arcade/machine/+/gameover" \
     --cafile emqx.ca \
     -u "your_username" -P "your_password"
   ```

3. Keep this terminal open to watch for messages!

### 3. Test Stripe Integration 💳

1. Install the Stripe CLI:

=== "Windows"
    Download from: https://github.com/stripe/stripe-cli/releases/latest
    
=== "Mac"
    ```bash
    brew install stripe/stripe-cli/stripe
    ```

=== "Linux"
    ```bash
    # Download latest linux tar.gz from Stripe CLI releases
    sudo tar -xvf stripe_X.X.X_linux_x86_64.tar.gz -C /usr/local/bin
    ```

2. Login to Stripe CLI:
   ```bash
   stripe login
   ```

3. Forward webhooks to your local app:
   ```bash
   stripe listen --forward-to localhost:5000/webhook
   ```

4. Test payment flow:

    a. Create a payment link by running this command:
    ```bash
    curl -X POST http://localhost:5000/create-payment-link \
      -H "Content-Type: application/json" \
      -d '{"machine_id":"test123"}'
    ```
    
    You'll get back a response that looks like this:
    ```json
    {
        "url": "https://checkout.stripe.com/c/pay/cs_test_..."
    }
    ```

    !!! info "What is a Payment Link?"
        A Stripe Payment Link is a hosted payment page that lets customers securely make payments. On your arcade cabinet, players will scan a QR code that leads to this page. [Learn more about Stripe Payment Links](https://stripe.com/docs/payment-links).
    
    b. Copy the URL from the response and paste it into your web browser. You'll see Stripe's payment page, just like your arcade players will see when they scan the QR code!
    
    c. Complete the test payment using these card details:
    
       * Card number: `4242 4242 4242 4242`
       * Expiry: Any future date
       * CVC: Any 3 digits
       * ZIP: Any 5 digits

    !!! tip "Test Cards"
        The `4242 4242 4242 4242` card number is a special test card that Stripe provides. It will always work in test mode but won't work in production. Perfect for testing!

### 4. Verify Full Flow 🔄

Time to test everything together! You'll need three terminal windows:

=== "Terminal 1 - Run Flask App"
    ```bash
    python app.py
    ```

=== "Terminal 2 - Watch MQTT Messages"
    ```bash
    mosquitto_sub -h your.emqx.cloud.broker -p 8883 \
      -t "arcade/machine/+/coinpulse" \
      -t "arcade/machine/+/gameover" \
      --cafile emqx.ca \
      -u "your_username" -P "your_password"
    ```

=== "Terminal 3 - Forward Stripe Webhooks"
    ```bash
    stripe listen --forward-to localhost:5000/webhook
    ```

Now let's test the complete flow:

1. Create and use a payment link:
   ```bash
   curl -X POST http://localhost:5000/create-payment-link \
     -H "Content-Type: application/json" \
     -d '{"machine_id":"test123"}'
   ```

2. Complete the test payment in your browser

3. Watch Terminal 2 for the MQTT coinpulse message

4. Send a game over signal:
   ```bash
   curl -X POST http://localhost:5000/gameover \
     -H "Content-Type: application/json" \
     -d '{"machine_id":"test123"}'
   ```

5. Watch Terminal 2 for the MQTT game over message

## Troubleshooting Common Issues 🔧

### API Issues
* **Can't start Flask**: Check if port 5000 is already in use
* **Environment variables**: Make sure `.env.local` is in the right place
* **Import errors**: Verify virtual environment is activated

### MQTT Issues
* **Connection refused**: Check broker address and port
* **Authentication failed**: Verify username and password
* **SSL/TLS errors**: Make sure you have the correct CA certificate

### Stripe Issues
* **Invalid API key**: Check your test API key in `.env.local`
* **Webhook errors**: Ensure webhook forwarding is running
* **Payment fails**: Verify you're using the correct test card

## Success Criteria ✨

Your local setup is working when you can:

1. ✅ Get a successful response from the status endpoint
2. ✅ Create a payment link
3. ✅ Complete a test payment
4. ✅ See the coinpulse MQTT message
5. ✅ Send a game over signal
6. ✅ See the game over MQTT message

!!! success "Ready for Deployment!"
    Once you've verified all these steps, your system is working correctly and you're ready to move on to containerization and deployment!

## Next Steps 🔜

Once everything is tested and working:

1. Save any test outputs you want to keep
2. Stop all your test processes (Flask, Stripe CLI, MQTT subscriber)
3. Make sure your changes are committed to Git
4. Move on to the deployment section where we'll containerize and deploy your working code!

[Continue to First Deployment →](first-deployment.md){ .md-button .md-button--primary }
[Need Help?](../troubleshooting/common-issues.md){ .md-button }