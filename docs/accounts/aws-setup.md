# Setting Up Your AWS Account

Welcome to the AWS (Amazon Web Services) setup guide! We'll use AWS Lambda to run the software that connects your arcade cabinet to the payment system. Don't worry - we'll walk through this step-by-step! :cloud:

## What is AWS Lambda? :thinking:

Let's understand what AWS Lambda does in your arcade system:

* It's a "serverless" service that runs our arcade software
* It listens for successful payments from Stripe
* When someone pays, it tells your cabinet to add credits
* You only pay for the tiny amount of time it runs (with a generous free tier!)

!!! note "Why Serverless? :cloud:"
    Serverless computing means you don't have to worry about managing servers. AWS Lambda automatically runs your code in response to events, like a payment being made. Here’s why we use it:

    * **No Server Management**: You don't need to set up or maintain servers. AWS handles all the infrastructure.
    * **Scalability**: Lambda automatically scales with the number of requests. Whether it's one game or a thousand, it adjusts to meet demand.
    * **Cost-Effective**: You only pay for the compute time you use. This is perfect for our arcade system, which only needs to run code when a payment is made.
    * **Focus on Code**: You can focus on writing your arcade software without worrying about the underlying hardware.

!!! info "AWS Lambda vs Stripe"
    * **AWS Lambda**: Runs our software that manages arcade credits
    * **Stripe**: Handles all the actual payment processing (credit cards, security, etc.)
    
    Think of Stripe as the cash register and AWS Lambda as the arcade operator who adds credits after seeing a successful payment!

## Before You Start :clipboard:

You'll need:

* An email address
* A phone number for verification
* About 15-20 minutes of time

!!! note "Account Verification"
    [!INSERT UPDATE NEEDED: Verify 2024 AWS account requirements]
    AWS may require account verification. We'll update this section with the latest requirements for free tier accounts.

## What's Included in Free Tier :moneybag:

AWS Free Tier gives you plenty for running your arcade system:

* 1 million Lambda function requests per month
   * (That's a lot of game credits being added!)
* 400,000 GB-seconds of compute time per month
   * (More than enough for several cabinets)
* Never expires for Lambda's core features

!!! success "Designed for Free Tier"
    Our arcade software is specifically designed to stay within AWS's free tier limits for normal use!

## Step-by-Step Setup :footprints:

### 1. Create Your Account

1. Visit [https://aws.amazon.com](https://aws.amazon.com)
2. Click the "Create an AWS Account" button
3. Enter your email address
4. Choose a password
5. Pick an AWS account name (like "MyArcadeProject")

[!INSERT SCREENSHOT: AWS signup page with arrows pointing to important fields]

### 2. Contact Information

* Fill in the required contact information
* Choose "Personal Account" type
* Read and accept the AWS Customer Agreement

!!! tip "Account Type"
    Choose "Personal" even if this is for school - it's simpler and still gives you everything you need!

### 3. Identity Verification

* Enter your phone number
* Choose how to receive your verification code (text or call)
* Enter the code when you receive it

[!INSERT SCREENSHOT: Identity verification screen with example (with sensitive info blocked out)]

### 4. Choose a Support Plan

* Select the "Basic Support - Free" tier
* You don't need paid support for this project
* You can always upgrade later if needed

## Setting Up Security :shield:

### Enable Multi-Factor Authentication (MFA)

This extra security step is really important!

1. Sign in to AWS Console
2. Click your account name in top right
3. Select "Security credentials"
4. Follow the "Activate MFA" steps

!!! danger "Don't Skip This Step!"
    MFA keeps your account safe. It prevents unauthorized access to your arcade system!

### Create an IAM User

Instead of using your root account (main account), we'll create a safer, limited-access account:

1. Open the IAM service
2. Create a new user
3. Give it a name (like "arcade-admin")
4. Choose "Access key - Programmatic access"

[!INSERT SCREENSHOT: IAM user creation with appropriate permissions]

## Free Tier Monitoring :chart_with_upwards_trend:

### Setting Up AWS Lambda Monitoring

Let's make sure you can track your usage:

1. Go to AWS Lambda Dashboard
2. View the monitoring tab
3. Set up basic monitoring alerts

### Setting Up Billing Alerts

Even though we're using the free tier, it's good practice to monitor usage:

1. Go to AWS Billing Dashboard
2. Create a billing alert
3. Set it to alert you if approaching free tier limits

!!! tip "Staying Free"
    Our arcade software is designed to stay within free tier limits for normal use. We'll show you how to monitor this in the next sections.

## Next Steps :arrow_forward:

After setting up your AWS account:

1. Keep your account credentials safe
2. Save the AWS account ID (you'll need it later)
3. Write down your IAM user details
4. Store the access keys securely

[Continue to Stripe Setup →](stripe-setup.md){ .md-button .md-button--primary }
[Back to Prerequisites](../getting-started/prerequisites.md){ .md-button }

## Troubleshooting :wrench:

Common setup issues and solutions:

### Can't Create Account
* Double-check email isn't already registered
* Clear browser cache and try again
* Use a different browser

### Can't Receive Verification Code
* Try an alternative phone number
* Switch between text and call options
* Contact AWS Support

### Account Activation Issues
* Usually resolves in 24 hours
* Check spam folder for AWS emails
* Verify all information is correct

### Lambda Function Issues
* Check function permissions
* Verify IAM roles are correct
* Monitor CloudWatch logs

!!! question "Need Help?"
    * Check our [Troubleshooting Guide](../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Visit AWS's help center
    * Contact [AWS Support](https://aws.amazon.com/support)

[!INSERT SECTION: Add common student success stories and gotchas]

## Understanding AWS Costs :money_with_wings:

### Free Tier Coverage

Our arcade system uses these AWS services:

1. AWS Lambda
    * 1M free requests per month
    * 400,000 GB-seconds compute time

2. API Gateway
    * 1M API calls per month
    * Built-in security features

### Monitoring Usage

Keep track of your usage through:

* AWS Billing Dashboard
* CloudWatch Metrics
* Lambda Monitoring
* Cost Explorer

!!! tip "Cost Management"
    The system is designed to use minimal resources. A typical arcade cabinet processing several games per day should stay well within free tier limits!

[!INSERT SECTION: Add typical usage patterns and cost estimates for different scenarios]
