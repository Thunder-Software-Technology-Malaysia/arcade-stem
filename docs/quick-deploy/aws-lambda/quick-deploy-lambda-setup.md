# Setting Up AWS Lambda

Welcome to the AWS Lambda setup guide! Now that you have the Docker image on your computer, let's get it running in the cloud! :zap:

## Prerequisites :clipboard:

Before starting, make sure you have:

* Completed [Basic AWS Setup](../accounts/aws/basic-setup.md)
* Successfully pulled and renamed the Docker image (previous step)
* AWS CLI installed and configured
* Your terminal or PowerShell still open

## Step 1: Push to Amazon ECR :arrow_up:

First, we need to get your Docker image into AWS's container registry (ECR):

1. Create an ECR repository:

    ```bash
    aws ecr create-repository --repository-name artcade-api-repo
    ```

2. Login to ECR (replace YOUR-REGION and YOUR-ACCOUNT-ID):

    ```bash
    aws ecr get-login-password --region YOUR-REGION | docker login --username AWS --password-stdin YOUR-ACCOUNT-ID.dkr.ecr.YOUR-REGION.amazonaws.com
    ```

3. Tag your image for ECR (make sure to replace YOUR-REGION and YOUR-ACCOUNT-ID):

    ```bash
    docker tag diy-artcade-payment-api:latest YOUR-ACCOUNT-ID.dkr.ecr.YOUR-REGION.amazonaws.com/artcade-api-repo:latest
    ```

4. Push to ECR (using the same YOUR-REGION and YOUR-ACCOUNT-ID):

    ```bash
    docker push YOUR-ACCOUNT-ID.dkr.ecr.YOUR-REGION.amazonaws.com/artcade-api-repo:latest
    ```

!!! info "About YOUR-REGION and YOUR-ACCOUNT-ID"
    * Replace YOUR-REGION with values like `us-east-1` or `us-west-2`
    * Replace YOUR-ACCOUNT-ID with your 12-digit AWS account number
    * Find both values in the top right of your AWS Console
    * Or run this command to find your account ID:
    ```bash
    aws sts get-caller-identity
    ```

!!! example "Command Example with Real Values"
    If your account ID is 123456789012 and region is us-east-1, your commands would look like:
    ```bash
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
    ```

## Step 2: Create Lambda Function :gear:

Now that your image is in ECR, let's create your Lambda function:

1. Go to AWS Console
2. Search for "Lambda"
3. Click "Create function"
4. Choose these settings:

    * Select "Container image"
    * Set function name to "artcade-api"
    * Click "Browse images"
    * Select the "artcade-api-repo" repository
    * Choose the "latest" tag
    * Click "Create function"

!!! info "What's Lambda?"
    AWS Lambda is like a smart worker in the cloud that:
    
    * Runs your arcade payment code
    * Only works when needed
    * Automatically handles multiple players
    * Stays within the free tier!

## Step 3: Configure Environment :wrench:

Your Lambda function needs some secret information to work:

1. In Lambda Console:
    * Click "Configuration" tab
    * Select "Environment variables"
    * Click "Edit"

2. Add these variables (you got these from previous setup steps):

    * `STRIPE_API_KEY`: Your Stripe secret key
    * `STRIPE_WEBHOOK_SECRET`: Your Stripe webhook secret
    * `MQTT_USERNAME`: Your EMQX username
    * `MQTT_PASSWORD`: Your EMQX password
    * `MQTT_BROKER`: Your EMQX broker address
    * `MQTT_PORT`: Usually 8883 for SSL/TLS
    * `PRICE_ID`: Your Stripe Price ID

!!! warning "Keep Secrets Safe!"
    Never share these values with anyone! They're like the keys to your arcade's payment system.

## Step 4: Test Your Function :test_tube:

Let's make sure everything works:

1. Click the "Test" tab
2. Create new test event:
    * Choose "API Gateway HTTP API" template
    * Name it "TestEvent"
    * Keep the default JSON
3. Click "Test"

You should see a successful response!

## Step 5: Monitor Your Function :chart_with_upwards_trend:

Set up basic monitoring:

1. Go to "Monitor" tab
2. View the CloudWatch metrics
3. Note the "Invocations" and "Errors" graphs

!!! success "Free Tier Limits"
    Your Lambda function gets:
    
    * 1 million free requests per month
    * 400,000 GB-seconds of compute time
    * Plenty for several arcade cabinets!

## Next Steps :arrow_forward:

Your Lambda function is ready! Next, we'll:

1. Set up API Gateway
2. Connect it to your Lambda
3. Test the complete system

[Continue to API Gateway Setup →](api-gateway-intro.md){ .md-button .md-button--primary }
[Back to Docker Pull](docker-pull.md){ .md-button }

## Troubleshooting :wrench:

### Common Issues

**Push to ECR Failed**
```bash
Error: Cannot push to ECR
```
* Check AWS CLI configuration
* Verify the repository name is exactly `artcade-api-repo`
* Try logging in to ECR again
* Make sure you replaced YOUR-REGION and YOUR-ACCOUNT-ID

**Lambda Creation Failed**
```bash
Error: Cannot create function
```
* Verify your image URI is correct
* Check IAM permissions
* Confirm the image was pushed to ECR successfully
* Make sure you're using the correct repository name

**Function Test Failed**
```bash
Error: Function error
```
* Check all environment variables are set correctly
* Look at CloudWatch logs for specific error messages
* Verify all secrets and credentials are correct

!!! question "Need Help?"
    * Check our [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Review CloudWatch logs in the "Monitor" tab