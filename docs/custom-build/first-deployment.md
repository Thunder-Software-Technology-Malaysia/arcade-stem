# Your First Deployment 🚀

Now that your code is tested and working locally, it's time to package it up and get it ready for AWS! We'll create a Docker container and push it to Amazon's Elastic Container Registry (ECR).

## What is Docker? 🐳

!!! info "Think of Docker Like This"
    Imagine you're moving to a new house:

    * Instead of moving furniture piece by piece, you put everything in a shipping container
    * The container has everything needed - furniture, appliances, decorations
    * The container works the same no matter what truck carries it
    
    Docker does the same thing for your code:
    
    * Instead of installing pieces separately, everything goes in a container
    * The container has your code, Python, libraries - everything it needs
    * The container runs the same way everywhere - your computer, AWS, anywhere!

## Prerequisites ✅

Before starting, make sure you have:

* [x] Locally tested code (from previous section)
* [x] Docker Desktop installed and running
* [x] AWS CLI installed and configured
* [x] Git repository with your latest code

!!! tip "Quick Docker Check"
    Run this command to verify Docker is working:
    ```bash
    docker --version
    ```
    If you see a version number, you're good to go!

## Step 1: Prepare Your Code 📝

1. Make sure your code is committed to Git:
   ```bash
   git status                  # Check what needs committing
   git add .                   # Add all changes
   git commit -m "Ready for deployment"  # Save changes
   ```

2. Verify your project structure:
   ```
   your-project/
   ├── app.py                 # Main application
   ├── requirements.txt       # Python dependencies
   ├── Dockerfile            # Docker configuration
   ├── .env.local            # Local environment variables
   └── ca.crt                # MQTT certificate
   ```

## Step 2: Build Your Docker Image 🏗️

1. Build your image locally:
   ```bash
   docker build --no-cache -t arcade-payment-api .
   ```

!!! note "What's Happening?"
    * `docker build` - Creates your container
    * `--no-cache` - Ensures fresh build
    * `-t arcade-payment-api` - Names your container
    * `.` - Uses current directory

2. Test your Docker image locally:
   ```bash
   docker run -p 8080:8080 arcade-payment-api
   ```

3. In another terminal, test the API:
   ```bash
   curl http://localhost:8080/status
   ```

   You should see:
   ```json
   {
     "status": "up",
     "message": "API is running"
   }
   ```

## Step 3: Prepare for AWS ECR 🌥️

1. Login to AWS ECR (replace `region` with your AWS region):
   ```bash
   aws ecr get-login-password --region region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.region.amazonaws.com
   ```

2. Create an ECR repository:
   ```bash
   aws ecr create-repository --repository-name arcade-payment-api --region region
   ```

3. Note your repository URI:
   ```
   your-account-id.dkr.ecr.region.amazonaws.com/arcade-payment-api
   ```

!!! tip "Finding Your Account ID"
    You can find your AWS account ID in the AWS Console or by running:
    ```bash
    aws sts get-caller-identity
    ```

## Step 4: Push to AWS ECR 📤

1. Tag your Docker image:
   ```bash
   docker tag arcade-payment-api:latest your-account-id.dkr.ecr.region.amazonaws.com/arcade-payment-api:latest
   ```

2. Push to ECR:
   ```bash
   docker push your-account-id.dkr.ecr.region.amazonaws.com/arcade-payment-api:latest
   ```

!!! info "Why Tag?"
    Tagging is like putting a shipping label on your container:

    * Tells Docker where to send it
    * Includes version information
    * Makes it easy to find in ECR

## Special Notes for M1/M2/M3 Mac Users 🍎

If you're using a newer Mac with Apple Silicon (M1, M2, or M3 chip):

1. Build for the right architecture:
   ```bash
   docker buildx build --platform linux/amd64 --no-cache -t arcade-payment-api .
   ```

2. Then continue with tagging and pushing as normal.

!!! tip "Why Different?"
    * New Macs use different processor architecture (ARM) than AWS (x86)
    * We need to build specifically for AWS's architecture
    * The `--platform` flag handles this for us

## Troubleshooting 🔧

### Common Docker Issues

* **Build Fails**

    * Check Dockerfile syntax
    * Verify all files are present
    * Look for Python dependency issues

* **Push Fails**

    * Check AWS credentials
    * Verify repository exists
    * Confirm login to ECR

* **Architecture Issues**

    * Use `--platform` flag on Apple Silicon
    * Check Docker Desktop settings
    * Verify AWS region settings

!!! question "Need Help?"
    * Review error messages carefully
    * Check [Docker logs](https://docs.docker.com/engine/reference/commandline/logs/)
    * See our [Troubleshooting Guide](../troubleshooting/common-issues.md)

## Success Criteria ✨

Your deployment is ready when:

1. ✅ Docker image builds successfully
2. ✅ Local container tests pass
3. ✅ Image is pushed to ECR
4. ✅ You can see your image in AWS Console

## Next Steps 🎯

Now that your container is in ECR:

1. Save your repository URI
2. Keep your environment variables handy
3. Get ready to set up your Lambda function!

[Set Up AWS Lambda →](aws-lambda/lambda-setup.md){ .md-button .md-button--primary }
[Back to Build and Test](build-and-test.md){ .md-button }
