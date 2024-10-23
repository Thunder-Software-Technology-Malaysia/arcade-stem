# Arcade STEM API with EMQX Serverless MQTT Integration

This repository contains a robust solution for managing arcade machine states and handling payments using a Flask API integrated with Stripe and EMQX for MQTT messaging. The API is containerized using Docker and deployed to AWS Lambda using an Amazon ECR (Elastic Container Registry) image. The MQTT broker is deployed in a serverless environment using EMQX, ensuring scalability and high performance without the need to manage underlying infrastructure.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Prerequisites](#2-prerequisites)
3. [Local Setup](#3-local-setup)
4. [EMQX Serverless Deployment](#4-emqx-serverless-deployment)
5. [Docker Setup for AWS Lambda Deployment](#5-docker-setup-for-aws-lambda-deployment)
6. [API Endpoints](#6-api-endpoints)
7. [MQTT Integration](#7-mqtt-integration)
8. [Testing](#8-testing)
9. [Stripe CLI Setup](#9-stripe-cli-setup)
10. [Troubleshooting](#10-troubleshooting)
11. [Notes](#11-notes)

## 1. Introduction

Welcome to the **Arcade STEM API** documentation integrated with **EMQX Serverless Deployment**. This guide provides a comprehensive setup for managing arcade machine states via MQTT and handling payments through Stripe. By leveraging serverless technologies, this setup ensures scalability, high performance, and reduced operational overhead.

- **Arcade STEM API:** A Flask-based API handling payments and arcade machine states.
- **Stripe Integration:** For managing payments and handling webhooks.
- **EMQX Serverless MQTT Broker:** For scalable and reliable MQTT messaging.
- **AWS Lambda & ECR:** For deploying the containerized API in a serverless environment.

## 2. Prerequisites

### 2.1 General Prerequisites

- **Docker Desktop:** Installed and running on your machine.
- **AWS CLI (Version 2):** Installed and configured to interact with your AWS account.
  ```shell
  aws configure
  ```
  You will be prompted to enter:
  - AWS Access Key ID
  - AWS Secret Access Key
  - Default region name (e.g., `ap-southeast-1`)
  - Default output format (e.g., `json`)
- **Python 3.6 or Higher**
- **VSCode (Recommended):** For an enhanced development experience.

### 2.2 EMQX Serverless Deployment Prerequisites

- **EMQX Cloud Account:** Sign up [Here](https://accounts.emqx.com/signin).
- **Network Permissions:** Ensure access to the internet and that no firewall rules block outbound communication on ports `1883` (MQTT), `8083` (WebSocket), `8883` (Secure MQTT), or other relevant ports.

## 3. Local Setup

### 3.1 Clone Repository

```shell
git clone https://github.com/Thunder-Software-Technology-Malaysia/arcade-stem.git
cd arcade-stem
```

### 3.2 Setup Virtual Environment in VSCode

1. Open the Project in VSCode:
   - Launch VSCode.
   - Click on File > Open Folder... and select the cloned arcade-stem repository.

2. Create a Virtual Environment:
   - Open the integrated terminal in VSCode (View > Terminal).
   - Run the following command:
     ```shell
     python3 -m venv venv
     ```
   Note: On Windows, you might use `python` instead of `python3`.

3. Activate the Virtual Environment:
   - macOS / Linux:
     ```shell
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate
     ```
   - Windows (Command Prompt):
     ```cmd
     venv\Scripts\activate.bat
     ```

4. Verify Activation:
   - The terminal prompt should now be prefixed with `(venv)`.

### 3.3 Install Dependencies

```shell
pip install -r requirements.txt
```

### 3.4 Configure Environment Variables

1. Create a `.env.local` file in the project root directory with the following variables:

```plaintext
STRIPE_API_KEY=your_stripe_api_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
STRIPE_PRICE_ID=your_stripe_price_id
MQTT_USERNAME=your_mqtt_username
MQTT_PASSWORD=your_mqtt_password
EMQX_BROKER_URL=your-emqx-broker-url
EMQX_PORT=8883
```

2. **Variable Descriptions:**
   - `STRIPE_API_KEY`: Your Stripe Secret API Key
   - `STRIPE_WEBHOOK_SECRET`: Your Stripe Webhook Secret
   - `STRIPE_PRICE_ID`: The Stripe Price ID for the product/service
   - `MQTT_USERNAME`: Username for MQTT broker authentication
   - `MQTT_PASSWORD`: Password for MQTT broker authentication
   - `EMQX_BROKER_URL`: URL of your EMQX broker
   - `EMQX_PORT`: Port for MQTT broker
   - `PRICE_ID` : Price_ID of the product

3. **Obtaining API Keys:**
   - Stripe API Key:
     - Sign in to your Stripe Dashboard
     - Navigate to Developers > API keys
     - Use the Secret key (starts with sk_test_ for testing)
   - Stripe Webhook Secret:
     - Obtained after setting up a webhook endpoint in Stripe
   - EMQX Credentials:
     - Sign up and deploy your MQTT broker using the EMQX Serverless Deployment Guide
     - Use the provided username and password

### 3.5 Run the Application

1. Start the Flask Application:
   ```shell
   python app.py
   ```

2. Test the status endpoint:
   ```shell
   curl http://localhost:5000/status
   ```

   Expected response:
   ```json
   {
     "status": "up",
     "message": "API is running"
   }
   ```

## 4. EMQX Serverless Deployment

### 4.1 Introduction

EMQX is a highly scalable, open-source MQTT messaging broker designed for IoT systems. Deploying EMQX in a serverless environment using EMQX Cloud ensures automatic scaling, high availability, and reduced operational management.

### 4.2 Setup Instructions

1. **Navigate to the EMQX Cloud Console**
2. **Log in or Create an Account**
3. **Create a New Deployment:**
   - Click on "Create Deployment"
   - Select "Serverless Deployment"
   - Choose a Cloud Provider and Region
4. **Configure Deployment Options:**
   - Set Deployment Name
5. **Launch the Deployment**
6. **SSL/TLS Configuration:**
   - Download CA Certificate
   - Configure secure connections

### 4.3 Testing the Deployment

**Publishing Example:**

# Publish coinpulse
```bash
mosquitto_pub -h your-emqx-broker-url -p 8883 \
  -t "arcade/machine/your-machine-id/coinpulse" \
  -m '{"machineId": "your-machine-id", "credits": 1, "timestamp": "timestamp-of-coinpulse"}' \
  --cafile "path/to/ca.crt" \
  -u "your-username" -P "your-password"
```

# Publish gameover
```bash
mosquitto_pub -h your-emqx-broker-url -p 8883 \
  -t "arcade/machine/your-machine-id/gameover" \
  -m '{"machineId": "your-machine-id", "status": "game_over", "timestamp": "timestamp-of-gameover"}' \
  --cafile "path/to/ca.crt" \
  -u "your-username" -P "your-password"
```

**Subscribing Example:**
```bash
mosquitto_sub -h your-emqx-broker-url -p 8883 \
  -t "arcade/machine/+/coinpulse" \
  -t "arcade/machine/+/gameover" \
  --cafile "path/to/ca.crt" \
  -u "your-username" -P "your-password"
```

### 4.4 Troubleshooting

- **Deployment Failed:**
  - Verify cloud provider region availability
- **Client Connection Issues:**
  - Check broker URL, port, and credentials
- **Firewall Restrictions:**
  - Verify required ports are open

## 5. Docker Setup for AWS Lambda Deployment

### 5.1 Prerequisites

- Amazon Elastic Container Registry (ECR)
- Docker Desktop
- AWS CLI (Version 2)

### 5.2 Finding Your Amazon ECR Repository

1. Log in to AWS Management Console
2. Navigate to ECR service
3. Create or use existing repository
4. Copy Repository URI

### 5.3 Deploy to AWS Lambda

1. **Build Docker Image:**
   ```shell
   docker build --no-cache -t arcade-game-app .
   ```

2. **Tag Docker Image:**
   ```shell
   docker tag arcade-game-app:latest your-account-id.dkr.ecr.your-region.amazonaws.com/arcade-game:latest
   ```

3. **Authenticate Docker to AWS ECR:**
   ```shell
   aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com
   ```

4. **Push Image to AWS ECR:**
   ```shell
   docker push your-account-id.dkr.ecr.your-region.amazonaws.com/arcade-game:latest
   ```

5. **Deploy to Lambda:**
   - Create Lambda function
   - Select container image
   - Configure environment variables
   - Set up API Gateway integration

### 5.4 Docker Build Architecture Issue on M3 MacBook Pro

**Problem:** Deployment fails with exec format error on M3 MacBooks.

**Solution:**
```shell
docker buildx build --platform linux/amd64 --no-cache -t arcade-game-app .
```

## 6. API Endpoints

### 6.1 Status Endpoint

- **URL:** `/status`
- **Method:** GET
- **Response:**
  ```json
  {
    "status": "up",
    "message": "API is running"
  }
  ```

### 6.2 Create Payment Link Endpoint

- **URL:** `/create-payment-link`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "machine_id": "unique_machine_id"
  }
  ```
- **Response:**
  ```json
  {
    "url": "https://payment-link.url"
  }
  ```

### 6.3 Stripe Webhook Endpoint

- **URL:** `/webhook`
- **Method:** POST
- **Description:** Handles Stripe events
- **Response:** 200 OK or 400 Error

### 6.4 Game Over Endpoint

- **URL:** `/gameover`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "machine_id": "unique_machine_id"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Game over signal sent"
  }
  ```

## 7. MQTT Integration

### 7.1 MQTT Topics

- `arcade/machine/<machine_id>/coinpulse`
- `arcade/machine/<machine_id>/gameover`

### 7.2 Publishing and Subscribing

Examples provided in [Testing the Deployment](#43-testing-the-deployment) section.

## 8. Testing

### 8.1 Testing with curl

**Create Payment Link:**
```bash
curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/prod/create-payment-link \
-H "Content-Type: application/json" \
-d "{\"machine_id\":\"your-machine-id\"}"
```

```bash
curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/prod/create-payment-link -H "Content-Type: application/json" -d "{\"machine_id\":\"your-machine-id\", \"price_id\":\"your-price-id\", \"quantity\":your-quantity}"
```

**Game Over Signal:**
```bash
curl -X POST https://your-api-id.execute-api.your-region.amazonaws.com/prod/gameover \
-H "Content-Type: application/json" \
-d "{\"machine_id\":\"your-machine-id\"}"
```

### 8.2 Setting up Stripe Webhook

1. Navigate to Stripe Dashboard Webhooks section
2. Add endpoint
3. Select events to monitor
4. Configure API Gateway URL
5. Create endpoint

## 9. Stripe CLI Setup

### Installing Stripe CLI

**macOS:**
```shell
brew install stripe/stripe-cli/stripe
```

**Windows:**
1. Download latest release from GitHub
2. Extract to desired location
3. Add to environment PATH

### Using Stripe CLI

**Forward Events:**
```shell
stripe listen --forward-to localhost:5000/webhook
```

## 10. Troubleshooting

- **Missing Environment Variables:**
  - Verify all variables in `.env.local`
- **Invalid Stripe API Keys:**
  - Check key validity
- **MQTT Connection Failures:**
  - Verify credentials and network settings
- **Docker Build Issues:**
  - Use correct architecture settings
- **API Gateway Integration:**
  - Check Lambda proxy integration
- **Webhook Verification:**
  - Verify webhook secrets
