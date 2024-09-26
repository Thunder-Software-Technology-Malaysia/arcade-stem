# Arcade STEM API

This repository contains a simple Flask API integrated with Stripe for handling payments and webhooks, and MQTT for managing arcade machine states. The API is containerized using Docker and deployed to AWS Lambda using an Amazon ECR (Elastic Container Registry) image.

## Endpoints

### Status Endpoint

### Create Payment Link Endpoint

- URL: /create-payment-link
- Method: POST
- Description: Create a Stripe Payment Link with optional machine metadata.
- Request Body:
  ```json
    "machine_id": "unique_machine_id"  // Optional machine ID to track the payment
  ```
- Response:
  ```json
    "url": "https://payment-link.url"  // URL to the payment link
  ```

- Testing with curl:
  - You can test the /create-payment-link endpoint using the following curl command:
    ```shell
    curl -X POST http://localhost:5000/create-payment-link -H "Content-Type:application/json" -d "{\"machine_id\":\"machine_123\"}"
    ```
### Stripe Webhook Endpoint

- URL: /webhook
- Method: POST
- Description: Stripe webhook to handle events such as payment completions.
- Request Body: Stripe sends the event payload automatically.
- Response:
```plaintext
  200 OK on success, 400 for validation errors
  ```

- Event Handling: The webhook listens for the checkout.session.completed event, verifies the event signature, and updates the status of the machine if machine_id is provided in the metadata.

- Testing Webhooks with Stripe CLI:
  - You can forward Stripe events to your local webhook using the following Stripe CLI command:
  ```shell
    stripe listen --forward-to localhost:5000/webhook
    ```

### Game Over Endpoint

- URL: /gameover
- Method: POST
- Description: Sends a game over signal to an arcade machine.
- Request Body:
  ```json
    "machine_id": "unique_machine_id"
  ```
- Response:
  ```json
  "message": "Game over signal sent"
    ```

## Local Setup

### Prerequisites

- Docker Desktop: Ensure Docker Desktop is installed and running on your machine.
- AWS CLI: Install the AWS CLI (version 2) and configure it to interact with your AWS account.
- AWS CLI Setup:
    aws configure
    You will be prompted to enter:
    - AWS Access Key ID
    - AWS Secret Access Key
    - Default region name (e.g., ap-southeast-1)
    - Default output format (e.g., json)

### Requirements

- Python 3.6 or higher
- Flask
- Stripe
- python-dotenv
- aws-wsgi
- paho-mqtt

### Local Setup

1. Clone the repository:
    ```shell
    git clone https://github.com/Thunder-Software-Technology-Malaysia/arcade-stem.git
    cd arcade-stem
    ```

2. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```

3. Create a .env.local file and add your Stripe API key and Webhook secret:
    ```plaintext
    STRIPE_API_KEY=your_stripe_api_key
    STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
    ```

4. Run the application:
    ```shell
    python app.py
    ```

## Docker Setup

1. Create a .env file in the root directory and add your keys:

```plaintext
STRIPE_API_KEY=your_stripe_api_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
```

2. Run Docker container locally:

3. Build and run the container using Docker:

```shell
docker build --no-cache -t arcade-game-app .
docker run --rm -d -p 5000:5000 --env-file .env --name arcade-stem-app arcade-game-app
```

4. Access the API locally at http://localhost:5000.

### Docker Setup for AWS Lambda Deployment

### Prerequisites

- Amazon Elastic Container Registry (ECR): AWS service to store your Docker images.
- Docker Desktop: Ensure it is installed and running.

### Finding Your Amazon ECR Repository

1. Log in to the AWS Management Console and navigate to the ECR service:

2. In the AWS Console, search for ECR (Elastic Container Registry).

3. You can create a new repository or use an existing one. For this project, ensure you have an ECR repository (e.g., arcade-game).

4. Copy the repository URI for use in the deployment steps (example: your-account-id.dkr.ecr.your-region.amazonaws.com/arcade-game).


## Deploy to AWS Lambda

### Step-by-Step AWS Lambda Docker Deployment

1. Build Docker image:

    ```shell
    docker build --no-cache -t arcade-game-app .
    ```

2. Tag the Docker image:

    -Tag your image with the AWS ECR repository URI:

    ```shell
    docker tag arcade-game-app:latest your-account-id.dkr.ecr.your-region.amazonaws.com/arcade-game:latest
    ```

3. Authenticate Docker to your AWS ECR:

    -Use the AWS CLI to log in to your ECR repository:

    ```shell
    aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com
    ```

4. Push the image to AWS ECR:

    ```shell
    docker push your-account-id.dkr.ecr.your-region.amazonaws.com/arcade-game:latest
    ```
Replace `your-account-id` and `your-region` with the actual AWS account ID and region where your ECR repository is located.

### Deploying Docker Image to AWS Lambda

1. Create an AWS Lambda function:

    Go to the AWS Lambda Console.
    Choose "Create Function" and select "Container image" as the source.
    Select the container image you uploaded to Amazon ECR (arcade-game:latest).

2. Set up environment variables in Lambda:

    In the AWS Lambda console, navigate to the configuration section and add the following environment variables:
    - STRIPE_API_KEY
    - STRIPE_WEBHOOK_SECRET (this will be filled in after setup the stripe webhook)

3. Link to API Gateway:

    -If you haven't already, set up an API Gateway to invoke your Lambda function.
    
    -Make sure to enable "Lambda Proxy Integration" when setting up the API Gateway routes for /create-payment-link, /webhook, and /gameover. 
    
    -This allows the API Gateway to forward all requests and responses between the Lambda function and the client.

### Setting up API Gateway with Proxy Integration

1. Create or open your API Gateway in the AWS Console.

2. Create a new route for the API, such as /create-payment-link and /webhook.

3. When adding the Lambda integration, ensure the Lambda Proxy Integration option is checked.

4. Deploy the API to make the routes live.

## MQTT Setup

### MQTT Integration in the API

The API uses MQTT to communicate with arcade machines after successful payments and game-over events. The MQTT broker used for testing is a public broker (test.mosquitto.org). The following MQTT topics are used:

- arcade/machine/<machine_id>/coinpulse: Sent when a payment is completed.
- arcade/machine/<machine_id>/gameover: Sent when the game over signal is triggered.

### Setting Up MQTT for Testing

#### Using mosquitto_sub to Subscribe to MQTT Topics

1. Install Mosquitto MQTT Client:

For Ubuntu:

```bash
sudo apt-get install mosquitto-clients
```

For macOS (using Homebrew):

```bash
    brew install mosquitto
```

For Windows: Download the Mosquitto client and install it.

2. Subscribe to the MQTT topics:

    Open a terminal and run the following command to subscribe to the relevant topics:
    ```bash
    mosquitto_sub -h test.mosquitto.org -p 1883 -t "arcade/machine/+/coinpulse" -t "arcade/machine/+/gameover"
    ```

This command subscribes to all coin pulse and game over topics from different machines using wildcards (+).

3. Publish messages (for testing purposes):

    To simulate MQTT messages manually, you can use mosquitto_pub to publish to the topics:

    ```bash
    mosquitto_pub -h test.mosquitto.org -p 1883 -t "arcade/machine/machine_123/coinpulse" -m '{"machineId": "machine_123", "credits": 10, "timestamp": "2024-01-01T00:00:00Z"}'
    ```

## Testing

### Testing with curl

- Create Payment Link: You can trigger the /create-payment-link API to generate a payment link using the following curl command:

    ```bash
    curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/prod/create-payment-link \ -H "Content-Type: application/json" \ -d "{\"machine_id\":\"machine_123\"}"
    ```

- Game Over Signal: You can trigger the /gameover API to send a game over signal using the following curl command:

    ```bash
    curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/prod/gameover \-H "Content-Type: application/json" \ -d "{\"machine_id\":\"machine_123\"}"
    ```


### Setting up Stripe Webhook on Stripe Dashboard with API Gateway

To configure a Stripe webhook via the Stripe Dashboard and connect it to your API Gateway, follow these steps:

1. Navigate to the Webhooks section in your Stripe Dashboard.

2. Click "Add endpoint."

3. Select the events you want to monitor. For this project, select the `checkout.session.completed` event.
    - You can search for the event and select it in the event filter section.

4. Add your API Gateway URL as the endpoint. The URL should be in the format:
https://{api_gateway_id}.execute-api.{region}.amazonaws.com/prod/webhook

Replace:
- {api_gateway_id} with your actual API Gateway ID.
- {region} with the AWS region your API Gateway is hosted in.

Example:
https://abc123.execute-api.us-east-1.amazonaws.com/webhook

5. Click "Create endpoint" to finalize the webhook setup.


## Stripe CLI Setup on Windows (Without Scoop)

To install the Stripe CLI on Windows without using Scoop:

1. Download the latest `windows` zip file from GitHub.
 
2. Unzip the `stripe_X.X.X_windows_x86_64.zip` file.

3. Add the path to the unzipped `stripe.exe` file to your `Path` environment variable. To learn how to update environment variables, see the Microsoft PowerShell documentation.

**Note:** Windows anti-virus scanners occasionally flag the Stripe CLI as unsafe. This is very likely a false positive. For more information, see issue #692 in the GitHub repository.
## Notes

- Make sure not to expose your Stripe API key and webhook secret publicly.
- This API is intended for educational purposes and should not be used in production without proper security measures.
