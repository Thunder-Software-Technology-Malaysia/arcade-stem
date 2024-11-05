# Configuration Options

Welcome to the configuration guide! Here you'll find all the settings you can adjust in your arcade system. Let's make your cabinet work exactly how you want it! :wrench:

## Environment Variables 🔑

These are the secret settings that control how your system works. You'll set these up in different places depending on whether you're testing locally or running in production.

### Core Settings (Required)

| Variable | Description | Example | Required? |
|----------|-------------|---------|-----------|
| `STRIPE_API_KEY` | Your Stripe secret API key | `sk_test_abc123...` | Yes |
| `STRIPE_WEBHOOK_SECRET` | Secret for verifying Stripe webhooks | `whsec_abc123...` | Yes |
| `PRICE_ID` | ID of your game credit product in Stripe | `price_abc123...` | Yes |
| `MQTT_USERNAME` | Username for EMQX connection | `arcade_user` | Yes |
| `MQTT_PASSWORD` | Password for EMQX connection | `your_password` | Yes |
| `MQTT_BROKER` | Your EMQX broker address | `broker.emqx.io` | Yes |
| `MQTT_PORT` | Port for MQTT connection (usually 8883 for SSL) | `8883` | Yes |

!!! warning "Protect Your Secrets!"
    Never share these values or commit them to Git! They should stay private and secure.

### Optional Settings

| Variable | Description | Default | Required? |
|----------|-------------|---------|-----------|
| `DEBUG` | Enable debug logging | `False` | No |
| `LOG_LEVEL` | Detail level for logging | `INFO` | No |
| `MAX_RETRIES` | Message retry attempts | `3` | No |

## Dynamic Parameters 🎮

### Machine ID

The `machine_id` is not an environment variable but a parameter you'll use in API requests:

1. Creating a Payment:
```json
POST /create-payment-link
{
    "machine_id": "unique_machine_id",
    "price_id": "optional_override",
    "quantity": "optional_override"
}
```

2. Sending Game Over:
```json
POST /gameover
{
    "machine_id": "unique_machine_id"
}
```

!!! tip "Choosing Machine IDs"
    Pick IDs that are:
    * Easy to remember (like `cab001`)
    * Unique to each cabinet
    * Simple but not guessable

## MQTT Topics 📡

### Topic Structure

All topics follow this pattern:
```
arcade/machine/<machine_id>/<message_type>
```

### Available Message Types

| Type | Purpose | Example Topic |
|------|---------|--------------|
| `coinpulse` | Credit signals | `arcade/machine/cab001/coinpulse` |
| `gameover` | Game completion | `arcade/machine/cab001/gameover` |

### Message Formats

1. Coin Pulse Signal:
```json
{
    "machineId": "unique_machine_id",
    "credits": 1,
    "timestamp": "2024-01-01T12:00:00Z"
}
```

2. Game Over Signal:
```json
{
    "machineId": "unique_machine_id",
    "status": "game_over",
    "timestamp": "2024-01-01T12:00:00Z"
}
```

## File Requirements 📁

### SSL/TLS Certificate

* **File**: `ca.crt`
* **Location**: Same directory as `app.py`
* **Purpose**: Secures MQTT connection

!!! danger "Certificate Security"
    * Keep your certificate file safe
    * Don't share it publicly
    * Update it when it expires
    * Back it up securely

## AWS Lambda Settings ⚡

### Basic Settings

| Setting | Recommended Value | Why? |
|---------|------------------|------|
| Memory | 128 MB | Sufficient for most operations |
| Timeout | 30 seconds | Allows for retry attempts |
| Concurrency | 5 | Good for multiple cabinets |

### Advanced Settings

| Setting | Recommended Value | Notes |
|---------|------------------|-------|
| Network | Create new VPC | Better security |
| Architecture | arm64 | Better cost/performance |
| SDK Log Level | INFO | Good for troubleshooting |

!!! info "Free Tier Usage"
    These settings are optimized to stay within AWS's free tier limits!

## Stripe Configuration 💳

### Webhook Settings

| Setting | Value | Required? |
|---------|-------|-----------|
| Endpoint URL | Your API URL + `/addCredit` | Yes |
| Events | `checkout.session.completed` | Yes |
| API Version | `2023-10-16` | Yes |

## Security Best Practices 🔒

1. **Credential Protection**
    * Never commit secrets to Git
    * Use environment variables
    * Keep certificates secure
    * Rotate credentials regularly

2. **Access Control**
    * Monitor access logs
    * Use strong machine IDs
    * Validate all inputs
    * Limit permissions

3. **Regular Updates**
    * Check for security updates
    * Update dependencies
    * Review access patterns
    * Monitor for unusual activity

!!! warning "Security First!"
    Remember: Security isn't just a feature - it's a requirement for handling payments!

## Testing Configuration 🧪

### Test Cards

| Card Number | Behavior |
|-------------|----------|
| 4242 4242 4242 4242 | Success |
| 4000 0000 0000 9995 | Decline |

### Test Environment

```ini
STRIPE_API_KEY=sk_test_...  # Use test key
DEBUG=True
LOG_LEVEL=DEBUG
```

## File Structure 📂

Your configuration files should be organized like this:

```
your-project/
├── app.py
├── ca.crt              # SSL certificate
├── .env.local          # Local environment variables
├── requirements.txt    # Python dependencies
└── README.md          # Documentation
```

!!! tip "Keep It Organized"
    Good organization makes troubleshooting easier!