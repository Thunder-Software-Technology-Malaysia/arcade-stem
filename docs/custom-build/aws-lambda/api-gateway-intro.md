# Understanding API Gateway

Welcome to the API Gateway guide! Let's learn about this important service that connects your arcade cabinet to your Lambda function. :bridge_at_night:

## What is API Gateway? :thinking:

Think of API Gateway as a smart receptionist for your arcade system:

* It receives requests from arcade cabinets
* Routes them to the right Lambda function
* Handles security and authentication
* Manages multiple connections
* Tracks usage and performance

!!! example "Real World Example"
    Imagine a hotel front desk:

    * Guests (arcade cabinets) arrive with requests
    * The receptionist (API Gateway) checks their ID
    * Then directs them to the right room (Lambda function)
    * Keeps track of who's visiting
    * Makes sure everything runs smoothly

## Why Do We Need It? :bulb:

API Gateway is essential because it:

1. Creates a stable URL for your API
2. Manages security and access
3. Handles multiple requests at once
4. Provides usage metrics
5. Stays within AWS free tier

!!! info "Free Tier Benefits"
    API Gateway's free tier includes:
    
    * 1 million API calls per month
    * Built-in DDoS protection
    * Request validation
    * Response caching

## API Gateway Concepts :books:

### 1. Endpoints

These are the URLs your arcade cabinet will use:

* `/status` - Check if system is running
* `/create-payment-link` - Generate QR codes
* `/addCredit` - Process payments
* `/gameover` - Handle game completion

### 2. Methods

Different types of requests:

* GET - Retrieve information
* POST - Send information
* PUT - Update information
* DELETE - Remove information

### 3. Stages

Different versions of your API:

* Development - For testing
* Production - For real use
* Custom stages - For special needs

### 4. Integrations

How API Gateway connects to Lambda:

* Proxy integration - Passes everything through
* Custom integration - More control but complex

## Security Features :lock:

API Gateway protects your system with:

1. Authentication
    * API keys
    * IAM roles
    * Custom authorizers

2. Throttling
    * Rate limiting
    * Burst limiting
    * Per-client limits

3. Monitoring
    * Request logging
    * Error tracking
    * Usage metrics

## Next Steps :arrow_forward:

Now that you understand API Gateway:

1. Set up your own API Gateway
2. Configure security settings
3. Test the integration

[Continue to API Gateway Setup →](setup-gateway.md){ .md-button .md-button--primary }
[Back to Lambda Setup](lambda-setup.md){ .md-button }

!!! tip "Keep Learning"
    * Explore API Gateway dashboard
    * Read CloudWatch logs
    * Test different configurations