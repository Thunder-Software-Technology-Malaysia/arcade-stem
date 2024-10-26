# Basic AWS Setup

Welcome to AWS (Amazon Web Services)! In this guide, we'll help you create and secure your AWS account. This is your first step toward getting your arcade cabinet connected to the cloud! :cloud:

## What You'll Set Up :clipboard:

In this guide, you'll:

* Create your AWS account
* Set up security features
* Configure basic monitoring
* Learn about AWS Free Tier

!!! note "Time & Requirements"
    **Time needed**: About 15-20 minutes

    **You'll need**:
    
    * An email address
    * A phone number
    * A credit/debit card (for verification only)
    * A computer with internet access

## Step-by-Step Account Creation :footprints:

### 1. Sign Up for AWS

1. Visit [https://aws.amazon.com](https://aws.amazon.com)
2. Click "Create an AWS Account"
3. Enter your email and AWS account name
    * Account name suggestion: "MyArcadeProject" or "MySTEMProject"
4. Choose a strong password

!!! tip "Choosing an Account Name"
    Pick something you'll remember but keep it professional - you might use this account for future projects too!

### 2. Fill in Contact Information

1. Select "Personal Account" type
2. Enter your contact information
3. Read and accept the AWS Customer Agreement

!!! info "Why Personal Account?"
    The Personal Account type gives you everything you need for this project and keeps things simple!

### 3. Add Payment Information

1. Enter your credit/debit card information
    * This is for verification only
    * We'll stay within free tier limits!
2. Complete the verification process

!!! warning "About Billing"
    Don't worry! Our project is designed to stay within AWS's free tier. We'll show you how to set up billing alerts just to be safe.

### 4. Verify Your Identity

1. Enter your phone number
2. Choose verification method (text or call)
3. Enter the verification code when received

### 5. Choose Support Plan

1. Select "Basic Support - Free"
2. Click "Complete sign up"

## Setting Up Security :shield:

### Enable Multi-Factor Authentication (MFA)

This extra security step is super important!

1. Sign in to AWS Console
2. Click your account name (top right)
3. Select "Security credentials"
4. Click "Assign MFA device"
5. Follow the setup wizard

!!! danger "Don't Skip MFA!"
    This keeps your account safe - kind of like having both a lock and an alarm on your front door!

### Create an IAM User

Instead of using your main account (root account), let's create a safer day-to-day account:

1. Go to IAM service in AWS Console
2. Click "Users" → "Add user"
3. Set up your admin user:
    * Username: "arcade-admin"
    * Select "Access key - Programmatic access"
    * Store your access keys safely!

## Setting Up Billing Alerts :bell:

Even though we're using the free tier, let's set up alerts:

1. Go to AWS Billing Dashboard
2. Click "Budgets"
3. Create a "Zero Spend Budget"
    * This alerts you if any charges occur

!!! success "Free Tier Usage"
    Our arcade project is specifically designed to stay within AWS's free tier limits for normal use!

## Next Steps :arrow_forward:

After completing this guide:

1. Save your AWS account ID
2. Store your IAM user credentials safely
3. Continue to Creating an AWS Container Registry

[Continue to Container Registry Setup →](container-registry.md){ .md-button .md-button--primary }

[Back to Getting Started](../../getting-started/prerequisites.md){ .md-button }

## Need Help? :sos:

Common setup issues:

* **Can't create account?** Double-check your email isn't already registered
* **Verification issues?** Try a different phone number or contact method
* **Card declined?** Make sure it's not expired and try another if needed

!!! question "Still Stuck?"
    * Check our [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Visit the [AWS Help Center](https://aws.amazon.com/premiumsupport/knowledge-center/)