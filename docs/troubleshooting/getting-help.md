# Getting Help

Welcome to the help guide! Everyone needs help sometimes - even experienced developers! Let's look at all the ways you can get assistance with your arcade cabinet project. :raising_hand:

## Quick Help Checklist :clipboard:

Before asking for help, try these quick steps:

1. Check the [Common Issues](common-issues.md) guide
2. Look through error messages carefully
3. Try searching for the error online
4. Review relevant documentation sections

!!! tip "Screenshots Help!"
    When asking for help, include screenshots of:
    
    * Error messages
    * Console output
    * Relevant code
    * AWS/Stripe dashboards

## Where to Get Help :compass:

### 1. Your Teacher/Mentor

Best for:
* Project requirements
* Business questions
* Local setup issues
* General guidance

!!! tip "Working with Your Mentor"
    * Schedule regular check-ins
    * Come prepared with specific questions
    * Take notes during meetings
    * Follow up on suggestions

### 2. Official Documentation

#### AWS Resources
* [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
* [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
* [AWS Free Tier Details](https://aws.amazon.com/free/)

#### Stripe Resources
* [Stripe Documentation](https://stripe.com/docs)
* [Stripe Testing Guide](https://stripe.com/docs/testing)
* [Stripe Support Center](https://support.stripe.com)

#### EMQX Resources
* [EMQX Cloud Documentation](https://docs.emqx.io/cloud/latest/)
* [MQTT Basic Concepts](https://docs.emqx.io/mqtt/latest/mqtt-concepts.html)
* [EMQX Support](https://docs.emqx.io/support)

### 3. Community Resources

Great places to find answers:

* Stack Overflow
    * Search for "[aws-lambda]" tag
    * Look for "[stripe-api]" questions
    * Check "[mqtt]" discussions

* GitHub Discussions
    * Review issues in similar projects
    * Check documentation updates
    * Look for community solutions

!!! warning "When Posting Questions"
    Never share:
    * API keys
    * Passwords
    * Secret tokens
    * Personal information

## How to Ask for Help :bulb:

### 1. Describe Your Problem

Include:
* What you're trying to do
* What's happening instead
* Any error messages
* Steps to reproduce

Example:
```markdown
Problem: Game won't start after payment
Expected: Game starts when payment completes
Actual: Cabinet stays in attract mode
Error: "No coin pulse received" in logs
```

### 2. Show What You've Tried

List the solutions you've attempted:

```markdown
Steps taken:
1. Checked MQTT connection
2. Verified Stripe webhook
3. Tested local API endpoint
4. Reviewed CloudWatch logs
```

### 3. Provide Context

Include relevant details:

* Your development environment
* AWS region being used
* Stage of the project
* Recent changes made

## Creating Support Tickets :ticket:

### AWS Support

1. Go to AWS Support Center
2. Click "Create case"
3. Choose "Service limit increase" or "Technical support"
4. Fill in the details

!!! note "AWS Support Levels"
    Free tier includes:
    * Basic support features
    * Service health checks
    * Documentation access
    * AWS Personal Health Dashboard

### Stripe Support

1. Visit Stripe Dashboard
2. Click "Support" in bottom left
3. Choose your topic
4. Describe your issue

!!! tip "Stripe Support Tips"
    * Include test API logs
    * Share webhook event IDs
    * Describe payment flow
    * Provide checkout session IDs

### EMQX Support

1. Access EMQX Cloud Console
2. Use "Help" or "Support" section
3. Describe connection issues
4. Include broker details

## Debugging Tools :wrench:

### Local Testing

```bash
# Test API endpoint
curl http://localhost:5000/status

# Monitor MQTT messages
mosquitto_sub -h your.emqx.broker -p 8883 \
  -t "arcade/machine/+/coinpulse" \
  --cafile emqx.ca \
  -u "your_username" -P "your_password"

# Forward Stripe webhooks
stripe listen --forward-to localhost:5000/webhook
```

### Cloud Monitoring

* AWS CloudWatch
* Stripe Dashboard Events
* EMQX Cloud Console

## Next Steps :footprints:

1. Check the [Common Issues](common-issues.md) guide first
2. Try solving it yourself using this guide
3. Ask your teacher/mentor if stuck
4. Use official support channels if needed

[Back to Common Issues](common-issues.md){ .md-button }
[Return to Tutorials](../tutorials/basic-setup.md){ .md-button .md-button--primary }

!!! success "You've Got This!"
    Remember: Every developer was a beginner once. Don't be afraid to ask for help - it's part of learning! :star: