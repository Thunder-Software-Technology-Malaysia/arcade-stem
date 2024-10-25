# Setting Up Your EMQX Account

Welcome to the EMQX setup guide! EMQX helps your arcade cabinet communicate with the payment system using something called MQTT messaging. Think of it like a super-fast mail service for your arcade! :envelope_with_arrow:

## What is EMQX? :thinking:

EMQX is a messaging system that helps different parts of your arcade talk to each other:

* Sends messages when someone pays
* Tells the game when to start
* Signals when a game is over
* Handles all this communication securely

!!! info "Why MQTT?"
    MQTT (the messaging protocol EMQX uses) is perfect for arcade machines because:
    
    * It's super fast (great for real-time gaming!)
    * Uses very little internet bandwidth
    * Works even with spotty internet connections
    * Used by millions of devices worldwide

## Before You Start :clipboard:

You'll need:

* An email address
* About 10-15 minutes
* Your AWS account details (from previous setup)

!!! tip "Keep Notes"
    Have a notepad ready to save important information like:
    * Broker URL
    * Port numbers
    * Username and password

## Signing Up :pen:

### 1. Create Your Account

1. Visit [https://accounts.emqx.com/signup](https://accounts.emqx.com/signup)
2. Enter your email address
3. Create a strong password
4. Verify your email

[!INSERT SCREENSHOT: EMQX signup page with important fields highlighted]

### 2. Create a Deployment

1. Log into EMQX Cloud Console
2. Click "Create Deployment"
3. Choose "Serverless" (it's free!)
4. Pick a name (like "MyArcadeMessaging")

!!! success "Free Tier Benefits"
    The free tier includes:

    * 1 million messages/month (plenty for your use)
    * 1 GB of traffic per month (way more than you will need)
    * Perfect for a stem team with 1 to 25 cabinets!

## Configuration :gear:

### Setting Up Your Broker

1. After deployment creation:
   * Save your **Broker URL**
   * Note the **Port Numbers**:
     * 1883 (MQTT)
     * 8883 (MQTT over SSL)
     * 8083 (WebSocket)

2. Create Authentication:
   * Go to "Authentication"
   * Create new credentials
   * Save your username and password

!!! danger "Keep Credentials Safe!"
    Your broker credentials are like keys to your arcade. Keep them private!

## Testing Your Connection :test_tube:

### Using MQTT Explorer (Optional)

1. Download MQTT Explorer
2. Connect using your credentials:
   ```
   Broker: your-broker.emqx.cloud
   Port: 8883
   Username: your-username
   Password: your-password
   ```

### Test Messages

Your arcade will use these message formats:

```json
# Coin Pulse (When credits are added)
{
    "machineId": "your-machine-id",
    "credits": 1,
    "timestamp": "2024-07-01T12:00:00Z"
}

# Game Over Signal
{
    "machineId": "your-machine-id",
    "status": "game_over",
    "timestamp": "2024-07-01T12:30:00Z"
}
```

## Understanding Topics :books:

MQTT uses "topics" to organize messages. Your arcade will use:

* `arcade/machine/<machine_id>/coinpulse`
* `arcade/machine/<machine_id>/gameover`

!!! example "Topic Examples"
    If your machine ID is "arcade123":
    * `arcade/machine/arcade123/coinpulse`
    * `arcade/machine/arcade123/gameover`

## Monitoring Your System :chart_with_upwards_trend:

### Dashboard Features

EMQX provides helpful monitoring:

* Connected clients
* Message traffic
* Error logs
* System status

[!INSERT SCREENSHOT: EMQX monitoring dashboard]

## Security Settings :shield:

### Enable SSL/TLS

For security:

1. Go to Deployment → Security
2. Enable TLS/SSL
3. Use port 8883 for secure connections
4. Download the CA certificate

!!! tip "SSL Security"
    Always use SSL in production! It keeps your arcade communications private and secure.

## Free Tier Limits :moneybag:

The EMQX platform offers a free tier with specific limits designed for users to explore its functionalities without incurring costs. Here are the key restrictions associated with the free tier:

* **Session Minutes:** 1 million session minutes per month.
* **Traffic:** 1 GB of traffic per month.
* **Client Connections:** The maximum number of client connections is not explicitly limited but is subject to overall performance constraints.
* **Message Size:** The maximum message size is capped at 1 MB (our messages are around 65 bytes each).
* **Message Queue Length:** The maximum message queue length is set at 1000 messages.
* **Session Expiry Time:** Sessions expire after 2 hours if inactive.
* **Retained Messages:** A maximum of 2000 retained messages, each up to 1 MB in size.
* **Subscriptions:** Each client can have a maximum of 10 subscriptions.

!!! success "Designed for Free Tier"
    Our arcade software is specifically designed to stay within these limits!

## Next Steps :arrow_forward:

After setting up EMQX:

1. Save your broker URL
2. Keep credentials secure
3. Test the connection
4. Ready for deployment!

[Continue to Quick Deploy Guide →](../quick-deploy/overview.md){ .md-button .md-button--primary }
[Back to Stripe Setup](stripe-setup.md){ .md-button }

## Troubleshooting :wrench:

Common issues and solutions:

### Connection Problems
* Check credentials
* Verify port numbers
* Ensure SSL is enabled
* Test network connectivity

### Message Not Received
* Verify topic names
* Check subscription status
* Monitor message logs
* Confirm client connection

!!! question "Need Help?"
    * Check our [Troubleshooting Guide](../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Visit [EMQX Docs](https://docs.emqx.com)
    * Contact EMQX Support

## Testing Tools :tools:

Useful tools for testing:

* MQTT Explorer
* Mosquitto CLI
* MQTT.fx
* EMQX Web Console

Example using Mosquitto CLI:
```bash
# Subscribe to topics
mosquitto_sub -h your-broker.emqx.cloud -p 8883 \
  -t "arcade/machine/+/coinpulse" \
  --cafile emqx.crt \
  -u "your-username" -P "your-password"

# Publish test message
mosquitto_pub -h your-broker.emqx.cloud -p 8883 \
  -t "arcade/machine/test123/coinpulse" \
  -m '{"machineId":"test123","credits":1,"timestamp":"2024-07-01T12:00:00Z"}' \
  --cafile emqx.crt \
  -u "your-username" -P "your-password"
```

!!! tip "Local Testing"
    These tools are great for testing your setup before connecting your arcade cabinet!
