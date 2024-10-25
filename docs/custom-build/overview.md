# Custom Build Overview

Welcome to the Custom Build Path! :rocket: This is where you'll learn to build your arcade payment system from scratch, giving you complete control over how it works.

## What You'll Build :hammer_and_wrench:

You're going to create a cloud-based system that:

* Generates QR codes for payments
* Processes payments securely with Stripe
* Sends signals to start and stop games
* Keeps track of credits and game sessions

!!! tip "Learning Opportunity"
    By building this yourself, you'll learn real-world programming skills that professional developers use every day!

## System Architecture :building_construction:

Your system will have these main components:

1. Payment API (Python + Flask)
    * Creates payment links
    * Processes successful payments
    * Manages game sessions
    * Runs in AWS Lambda

2. Messaging System (MQTT)
    * Sends signals between components
    * Controls when games start/stop
    * Manages arcade cabinet state

3. Docker Container
    * Packages your code
    * Makes deployment easy
    * Runs consistently everywhere

[!INSERT IMAGE: Basic architecture diagram showing components]

## Technical Stack :gear:

Here's what we'll use to build the system:

### Programming Language

* Python 3.9
    * Easy to learn
    * Powerful libraries
    * Great for APIs

### Web Framework

* Flask
    * Lightweight
    * Easy to understand
    * Perfect for APIs

### Payment Processing

* Stripe
    * Handles payments securely
    * Creates payment links
    * Processes credit cards

### Message Broker

* MQTT with EMQX
    * Sends signals between components
    * Fast and reliable
    * Industry standard

### Containerization

* Docker
    * Packages your code
    * Makes deployment easy
    * Works everywhere

### Cloud Platform

* AWS Lambda
    * Runs your code in the cloud
    * Scales automatically
    * Stays in free tier

## Project Structure :file_folder:

Here's how our project files are organized:

```
arcade-payment-api/
│
├── app.py              # Main application code
├── Dockerfile          # Instructions for building Docker image
├── requirements.txt    # Python package dependencies
├── ca.crt             # SSL certificate for MQTT
└── .env.local         # Local environment variables
```

## The Build Process :construction:

You'll build this system in these stages:

1. Set Up Development Environment
    * Install required software
    * Configure your editor
    * Set up version control

2. Create the Payment API
    * Build Flask application
    * Integrate Stripe payments
    * Handle webhooks

3. Add MQTT Messaging
    * Set up MQTT client
    * Implement signal handling
    * Test messaging

4. Containerize the Application
    * Create Docker container
    * Build the image
    * Test locally

5. Deploy to AWS
    * Configure AWS Lambda
    * Push container image
    * Set up API Gateway

## Required Knowledge :books:

Here's what you should know (or be ready to learn):

### Must Have

* Basic Python syntax
* Command line basics
* Git fundamentals

### Will Learn

* API development
* Cloud services
* Docker containers
* Payment processing
* Message queuing

!!! tip "New to Programming?"
    Don't worry if some of this looks unfamiliar! We'll explain everything step-by-step.

## Environment Setup :computer:

You'll need these tools installed:

1. Python 3.9+
2. Visual Studio Code
3. Docker Desktop
4. Git

!!! note "System Requirements"
    * 8GB RAM minimum
    * 10GB free disk space
    * Reliable internet connection

## Next Steps :arrow_forward:

Ready to start building? Here's what to do next:

1. [Understanding the Code](code-overview.md) - Learn how the system works
2. [Making Changes](modifications.md) - Customize the system
3. [Building & Deploying](deployment.md) - Get your code running

## Getting Help :sos:

If you get stuck:

* Check our [Troubleshooting Guide](../troubleshooting/common-issues.md)
* Ask your teacher or mentor
* Review the code comments
* Look up error messages

!!! question "Need Help?"
    Remember: Getting stuck is normal when learning to code. Don't be afraid to ask for help!

## Example Projects :star:

Here are some ways students have extended this project:

* Adding custom game modes
* Creating admin dashboards
* Implementing player stats
* Building tournament systems

[Continue to Code Overview →](code-overview.md){ .md-button .md-button--primary }
[Back to Choose Your Path](../getting-started/deployment-options.md){ .md-button }