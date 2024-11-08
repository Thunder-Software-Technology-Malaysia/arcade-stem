# Arcade STEM Docker Guide

This Docker image provides a ready-to-run environment for the Arcade STEM application that connects to Stripe and an MQTT broker. This image allows users to run the application by simply providing their own `.env` file and `.crt` certificate file.

## Prerequisites

- Docker installed on your local machine
- A valid `.env` file with the necessary configuration variables (detailed below)
- A `.crt` certificate file to establish secure connections

## Required Files

### `.env` File

The `.env` file must contain the following keys for the application to function:

```plaintext
STRIPE_API_KEY=your_stripe_api_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
MQTT_USERNAME=your_mqtt_username
MQTT_PASSWORD=your_mqtt_password
MQTT_BROKER=your_mqtt_broker_url
MQTT_PORT=your_mqtt_port
PRICE_ID=your_price_id
```

### `ca.crt` File

This `.crt` file should be named `ca.crt` and must be placed in the same directory from which you will run the Docker container. This file is essential for secure connections with the MQTT broker.

## How to Run the Docker Container

### Step 1: Pull the Docker Image

First, pull the Docker image from Docker Hub:

```bash
docker pull yeeyon/arcade-stem:latest
```

### Step 2: Prepare Your `.env` and `ca.crt` Files

1. Create or move your `.env` file with the required environment variables into a secure directory
2. Place your `ca.crt` file in the same directory as your `.env` file

### Step 3: Run the Docker Container

To run the container with your `.env` file and the `ca.crt` certificate, use the following command:

```bash
docker run --env-file /path/to/your/.env -v /path/to/your/ca.crt:/app/ca.crt -p 5000:5000 yeeyon/arcade-stem:latest
```

- Replace `/path/to/your/.env` with the path to your `.env` file
- Replace `/path/to/your/ca.crt` with the path to your `ca.crt` file
- Ensure that `yeeyon/arcade-stem:latest` matches the Docker image name

### Explanation of the Command

- `--env-file /path/to/your/.env`: Loads environment variables from your `.env` file
- `-v /path/to/your/ca.crt:/app/ca.crt`: Mounts your local `ca.crt` file to the container's `/app/ca.crt`
- `-p 5000:5000`: Maps port 5000 of the container to port 5000 of the host (adjust this if your application uses a different port)

## Environment Variable Details

| Variable | Description |
|----------|-------------|
| `STRIPE_API_KEY` | Your Stripe API Key for authenticating requests |
| `STRIPE_WEBHOOK_SECRET` | Your Stripe webhook secret for validating webhook requests |
| `MQTT_USERNAME` | MQTT broker username |
| `MQTT_PASSWORD` | MQTT broker password |
| `MQTT_BROKER` | URL of the MQTT broker |
| `MQTT_PORT` | Port number for the MQTT broker connection |
| `PRICE_ID` | Stripe price ID for handling payments |

**Make sure to keep your `.env` file secure as it contains sensitive information.**

## Notes

- This container is built on top of Python 3.9
- Be sure to update your `.env` variables to match your specific environment
- If any dependencies in `requirements.txt` are updated, rebuild the Docker image before re-running

## Troubleshooting

### Missing `.env` File Error

If you get an error indicating a missing `.env` file, double-check the `--env-file` path and make sure the `.env` file is properly formatted.

### Missing `ca.crt` File Error

Ensure the `ca.crt` file is correctly mounted by verifying the `-v` path. The file should be in the same directory as the `.env` file, or adjust the path accordingly.

### Connection Issues with MQTT

Check that your MQTT credentials and broker URL are correct. Ensure the broker is accessible from your network.