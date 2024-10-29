# Setting Up AWS Lambda

Welcome to the AWS Lambda setup guide! This is where we'll create the cloud API that powers your arcade cabinet. This API handles everything from payments to game control! :zap:

!!! warning "Important: Read First!"
    You can only complete this guide AFTER you have:

    * Either pulled the pre-built Docker image ([Quick Deploy](../../quick-deploy/overview.md))
    * OR built your own image ([Custom Build](../../custom-build/overview.md))
    * AND pushed the image to your [Container Registry](container-registry.md)

## What is AWS Lambda? :thinking:

AWS Lambda hosts your Artcade API in the cloud. Think of it as your arcade's brain that:

* Processes payments from Stripe
* Sends "coin pulse" signals to start games
* Handles "game over" signals
* Creates payment QR codes
* Monitors cabinet status
* Manages multiple arcade machines

!!! info "Why Lambda for Our API?"
    * No servers to manage - AWS handles everything
    * Only pay when your API is actually being used
    * Automatically handles multiple cabinets
    * Built-in security and monitoring
    * Perfect for APIs that handle occasional requests

## Prerequisites :clipboard:

Before starting, ensure you have:

* Completed [Basic AWS Setup](basic-setup.md)
* Set up your [Container Registry](container-registry.md)
* Docker image ready in your registry
* IAM user with Lambda permissions

## Creating Your Lambda Function :wrench:

### STEP 1. Open Lambda Service

1. Sign in to AWS Console
2. Search for "Lambda"
3. Click "Create function"

### STEP 2. Configure Function

1. Select "Container image"
2. Set function name to "artcade-api"
3. Select your container image URI from the registry
4. Click "Create function"

### STEP 3. Configure Environment Variables

1. Navigate to the Configuration tab
2. Click on Environment Variables
3. Add the following variables:
    * `STRIPE_API_KEY`: Your Stripe secret key
    * `STRIPE_WEBHOOK_SECRET`: Your Stripe webhook secret
    * `MQTT_USERNAME`: Your EMQX username
    * `MQTT_PASSWORD`: Your EMQX password
    * `MQTT_BROKER`: Your EMQX broker address
    * `MQTT_PORT`: Usually 8883 for SSL/TLS connection
    * `PRICE_ID`: Your Stripe Price ID for the game

!!! warning "Security Best Practices"
    Always use AWS Secrets Manager or AWS Systems Manager Parameter Store for sensitive information like API keys and passwords in a production environment.

## Testing Your Lambda :test_tube:

1. Navigate to the Test tab
2. Create a new test event
3. Select API Gateway HTTP API template
4. Save and run the test
5. Check results in the execution log

## Monitoring Setup :chart_with_upwards_trend:

1. Set Up CloudWatch Monitoring

    1. Navigate to CloudWatch in AWS Console
    2. Create alarms for:
        * Error rates
        * Function duration
        * Invocation counts
    3. Set notification thresholds

!!! success "Free Tier Limits"
    * 1M free requests per month
    * 400,000 GB-seconds compute time
    * Perfect for arcade cabinets!

## Next Steps :arrow_forward:

Once your Lambda function is set up, you'll need to:

1. Understand how API Gateway works
2. Configure API Gateway for your Lambda
3. Test the complete system

[Continue to API Gateway Introduction →](api-gateway-intro.md){ .md-button .md-button--primary }
[Back to Container Registry](container-registry.md){ .md-button }

## Troubleshooting :wrench:

Common Lambda issues:

1. **Container errors**: 
    * Check your Docker image
    * Verify the image URI
    * Look at CloudWatch logs

2. **Permission errors**: 
    * Check IAM roles
    * Verify execution permissions
    * Review security settings

3. **Environment issues**:
    * Verify all variables are set
    * Check for typos in values
    * Confirm secrets are properly stored

!!! question "Need Help?"
    * Check [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Review CloudWatch logs
    * Ask your teacher or mentor