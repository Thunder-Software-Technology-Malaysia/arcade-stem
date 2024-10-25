# Setting Up Your Stripe Account

Welcome to the Stripe setup guide! Stripe is what makes it possible for your arcade cabinet to accept payments. It's the same system many popular websites use for payments. Let's get it set up! :credit_card:

## What is Stripe? :thinking:

Stripe handles all the payment processing for your arcade cabinet:

* Creates QR codes for payments
* Processes credit/debit card payments securely
* Sends successful payment messages to API (which sends it to your gaming cabinet)
* Provides a dashboard to track earnings

!!! info "Stripe's Role"
    When someone wants to play your arcade:
    
    1. They scan a QR code on the cabinet
    2. Stripe shows them a payment page
    3. They pay securely with their phone
    4. Stripe tells AWS to add credits to your cabinet
    5. Game time! :video_game:

## Test Mode vs Live Mode :test_tube:

Stripe has two modes:

### Test Mode
* Perfect for development and testing
* Use fake credit card numbers
* No real money involved
* Great for learning and setup

### Live Mode
* For real payments when you're ready
* Requires business verification
* Involves real money
* Used when your arcade goes public

!!! tip "Start with Test Mode"
    We'll use Test Mode while setting everything up. This lets you practice and test without using real money!

## Setting Up Your Account :wrench:

### 1. Create Your Account

1. Visit [https://dashboard.stripe.com/register](https://dashboard.stripe.com/register)
2. Enter your email address
3. Create a secure password
4. Verify your email address

[!INSERT SCREENSHOT: Stripe registration page with important fields highlighted]

### 2. Account Settings

After registering:

* Choose your country/region
* Select "Individual" account type
* Pick "Test Mode" for now

!!! warning "Country Selection"
    Make sure to pick the correct country - this can't be changed later!

### 3. Get Your API Keys

1. Go to Developers → API Keys in dashboard
2. You'll see two keys:
    * Publishable Key (starts with 'pk_test_')
    * Secret Key (starts with 'sk_test_')

!!! danger "Keep Keys Secret!"
    Never share your Secret Key! The Publishable Key is okay to share, but the Secret Key must stay private.

[!INSERT SCREENSHOT: API keys page with sensitive information blocked out]

## Setting Up Products :shopping_cart:

### Create a Game Credits Product

1. Go to Products → Add Product
2. Set up your game credit options:
    * Name (e.g., "Arcade Credits")
    * Description
    * Price points
    * Currency

Example Setup:
```
Name: Arcade Credits
Description: Credits for arcade play
Price: $1.00
Type: One-time payment
```

[!INSERT SCREENSHOT: Product creation page with example fields filled]

## Test Your Setup :microscope:

### Using Test Card Numbers

Test your payment system with these card numbers:

* Success: 4242 4242 4242 4242
* Decline: 4000 0000 0000 0002
* Error: 4000 0000 0000 9995

!!! tip "Test Card Details"
    * Use any future expiry date
    * Any 3-digit CVC
    * Any ZIP code

## Monitoring Payments :chart_with_upwards_trend:

### Test Mode Dashboard

Watch your test payments in the dashboard:

* See successful/failed payments
* View payment details
* Track testing progress

[!INSERT SCREENSHOT: Test mode dashboard overview]

## Going Live :rocket:

When you're ready for real payments:

### 1. Complete Account Information
* Business details
* Bank account for deposits
* Tax information
* Identity verification

### 2. Switch to Live Mode
* Get live API keys
* Update your system configuration
* Test with a real payment

!!! warning "Before Going Live"
    Make sure to:
    * Test thoroughly in test mode
    * Have all business paperwork ready
    * Understand fees and pricing
    * Set up proper monitoring

## Understanding Stripe Fees :moneybag:

### Test Mode
* Completely free
* No real money involved
* Unlimited testing

### Live Mode
Standard fees:
* 2.9% + $0.30 per successful charge
* Example: On a $1.00 game play:
    * Fee: $0.33 ($0.029 + $0.30)
    * You receive: $0.67

!!! tip "Pricing Strategy"
    Consider Stripe fees when setting your game prices!

## Next Steps :arrow_forward:

After setting up Stripe:

1. Save your API keys safely
2. Test the payment flow
3. Set up your products
4. Try some test transactions

[Continue to EMQX Setup →](emqx-setup.md){ .md-button .md-button--primary }
[Back to AWS Setup](aws-setup.md){ .md-button }

## Troubleshooting :wrench:

Common issues and solutions:

### Payment Testing Issues
* Double-check test card numbers
* Verify API keys are correct
* Check webhook settings
* Monitor test mode logs

### Account Setup Problems
* Verify email address
* Check country settings
* Confirm product configuration
* Review API key access

!!! question "Need Help?"
    * Check our [Troubleshooting Guide](../troubleshooting/common-issues.md)
    * Ask your teacher or mentor
    * Visit [Stripe Support](https://support.stripe.com)
    * Review Stripe's documentation

[!INSERT SECTION: Add common student success stories and gotchas]

## Local Testing Tips :computer:

### Using Stripe CLI

The Stripe CLI helps test locally:

1. Install Stripe CLI
2. Run webhook forwarding
3. Test payments locally

!!! tip "Testing Locally"
    We'll cover detailed testing in the tutorials section!

## Security Best Practices :lock:

Remember to:

* Keep API keys secure
* Use test mode for development
* Monitor your dashboard
* Set up alerts for unusual activity
* Regularly review transactions

!!! success "Ready to Test?"
    Once your Stripe account is set up, you're ready to start testing payments with your arcade cabinet!