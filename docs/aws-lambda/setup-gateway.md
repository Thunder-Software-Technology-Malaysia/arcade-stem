# Setting Up API Gateway

Time to connect your Lambda function to the internet! We'll start by creating the API Gateway trigger and then set up each endpoint. :electric_plug:

## Getting started: Create API Gateway Trigger :key:

First, create the API Gateway trigger from your Lambda function:

1. Go to your Lambda function in AWS Console
2. Click on the "Configuration" tab
3. Select "Triggers" from the left menu
4. Click "Add trigger"
5. In the trigger configuration:

    * Select "API Gateway" from the dropdown
    * Under "API", select "Create an API"
    * Choose "HTTP API" (it's simpler and cheaper!)
    * For "Security", select "Open"

6. Click "Add" to create the trigger

!!! info "About HTTP APIs"

    HTTP APIs are perfect for our arcade because:

    * They're cost-effective
    * They're simpler to manage
    * They have great performance
    * They work well with Lambda

## Creating Resources and Methods :wrench:

### Step 1: Create a New Resource

1. Click "Create resource" button
2. In the resource setup:

    * Set Resource Path to "/" (root)
    * Give your resource a name that matches an endpoint in your code
    * Leave "Proxy Resource" and "CORS" unchecked

3. Click "Create resource"

!!! tip "Resource Names"

    Your resource name should match the endpoints in your code:

    * /status
    * /create-payment-link
    * /addCredit
    * /gameover

### Step 2: Create and Configure Method

After creating your resource:

1. Click on your newly created resource in the left sidebar
2. Click "Create method" button
3. In the method setup:

    * Choose the appropriate HTTP method (GET, POST) from dropdown
    * Select "Lambda Function" for Integration type
    * Enable "Lambda Proxy integration"
    * Select your Lambda function from the dropdown

4. Click "Create method"

!!! warning "Important Settings"

    Make sure you:

    * Choose the correct HTTP method for each endpoint
    * Select Lambda Function integration type
    * Enable Lambda Proxy integration
    * Select your specific Lambda function

### Step 3: Repeat for Each Endpoint

Create resources and methods for each endpoint:

1. Status Endpoint:

    * Resource path: /status
    * Method: GET

2. Payment Link Endpoint:

    * Resource path: /create-payment-link
    * Method: POST

3. Add Credit Endpoint:

    * Resource path: /addCredit
    * Method: POST

4. Game Over Endpoint:

    * Resource path: /gameover
    * Method: POST

## Deploying Your API :rocket:

After creating all resources and methods:

1. Click the "Deploy API" button
2. In the deployment popup:

    * Select "[New Stage]" if this is your first deployment
    * Enter a stage name (or leave as "default")
    * Add a description if you want

3. Click "Deploy"

!!! success "Get Your URL"

    After deployment, you'll get a URL that looks like:

    ```
    https://abc123def.execute-api.us-west-2.amazonaws.com/default
    ```
    
    Save this URL - you'll need it for:

    * Testing your API
    * Setting up Stripe webhooks
    * Configuring your arcade cabinet

## Testing Your Setup :test_tube:

Test each endpoint using your new API URL:

### 1. Status Check

```bash
curl https://your-api-url/status
```

### 2. Payment Link Creation

```bash
curl -X POST https://your-api-url/create-payment-link \
  -H "Content-Type: application/json" \
  -d '{"machine_id":"test123"}'
```

### 3. Game Over Signal

```bash
curl -X POST https://your-api-url/gameover \
  -H "Content-Type: application/json" \
  -d '{"machine_id":"test123"}'
```

## Troubleshooting :wrench:

Common issues and solutions:

### Method Not Found

* Check that you created the resource correctly
* Verify HTTP method matches your code
* Ensure Lambda proxy integration is enabled

### Lambda Permission Error

* Check that API Gateway has permission to invoke Lambda
* Verify Lambda function name is correct
* Review IAM roles and permissions

### Deployment Issues

* Make sure all methods are properly configured
* Check that you've deployed to a stage
* Verify the API URL you're using matches your deployment stage

!!! question "Need Help?"

    * Check [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Review CloudWatch logs
    * Ask your teacher or mentor

## Next Steps :arrow_forward:

After deploying your API:

1. Save your API URL
2. Update Stripe webhook settings
3. Test all endpoints
4. Monitor for issues

[Continue to Testing →](test-deployment.md){ .md-button .md-button--primary }
[Back to API Gateway Introduction](api-gateway-intro.md){ .md-button }