# Creating an AWS Container Registry

Let's set up your AWS Container Registry! This is where we'll store the Docker image for your arcade cabinet software. Think of it like a secure storage locker for your code! :package:

## What is a Container Registry? :thinking:

A container registry is like a special warehouse for storing your software:

* It keeps your Docker images safe and organized
* Makes it easy to deploy your software to AWS
* Helps manage different versions of your code

!!! info "What's a Docker Image?"
    A Docker image is like a blueprint for your software. It contains everything needed to run your arcade cabinet's payment system!

## Prerequisites :clipboard:

Before starting, make sure you have:

* Completed [Basic AWS Setup](basic-setup.md)
* AWS CLI installed on your computer
* Your IAM user access keys handy

!!! tip "Need AWS CLI?"
    Visit our [AWS CLI Setup Guide](../../tutorials/aws-cli-setup.md) if you haven't installed it yet!

## Creating Your Registry :wrench:

### 1. Open Amazon ECR

    1. Sign in to AWS Console
    2. Search for "ECR" in the services search bar
    3. Click "Amazon Elastic Container Registry"

### 2. Create a Repository

    1. Click "Create repository"
    2. For repository settings:
        * Visibility: "Private"
        * Repository name: "arcade-payment-system"
        * Tag immutability: Leave disabled
        * Scan on push: Enable
    3. Click "Create repository"

!!! note "About Repository Name"
    Choose a clear, descriptive name - you might create more repositories for future projects!

### 3. Configure Access

Make sure your IAM user has permission to use ECR:

1. Go to IAM service
2. Select your "arcade-admin" user
3. Add "AmazonEC2ContainerRegistryFullAccess" policy

## Using Your Registry :rocket:

### View Registry Details

1. Click your new repository
2. Note the Registry URI - you'll need this later!
   * Looks like: `123456789012.dkr.ecr.region.amazonaws.com/arcade-payment-system`

### Authentication Setup

Run these commands in your terminal:

```bash
# Configure AWS CLI with your credentials
aws configure

# Login to ECR
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-registry-uri
```

!!! warning "Replace Values!"
    * Change `your-region` to your AWS region (e.g., us-west-2)
    * Change `your-registry-uri` to your actual registry URI

## Next Steps :arrow_forward:

Your container registry is ready! Keep your Registry URI handy - you'll need it when you:

* Follow the [Quick Deploy Guide](../../quick-deploy/overview.md)
* Or build your own version in the [Custom Build Guide](../../custom-build/overview.md)

[Continue to Lambda Setup →](lambda-setup.md){ .md-button .md-button--primary }
[Back to Basic Setup](basic-setup.md){ .md-button }

## Troubleshooting :wrench:

Common issues:

* **Permission denied?** Check your IAM user permissions
* **Login failed?** Verify your AWS CLI configuration
* **Can't create repository?** Make sure you're in the right region

!!! question "Need Help?"
    * See [Troubleshooting Guide](../../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Check AWS ECR documentation
