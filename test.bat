@echo off

REM Step 1: Create a PaymentIntent and save the response to a file
curl -X POST https://api.stripe.com/v1/payment_intents -u sk_test_4eC39HqLyjWDarjtT1zdp7dc: -d amount=1000 -d currency=usd -d payment_method_types[]=card > response.json

REM Step 2: Extract the PaymentIntent ID from the response manually using findstr and substr
for /f "tokens=2 delims=:," %%a in ('findstr /i "id" response.json') do (
    set payment_intent_id=%%a
    goto :confirm_payment_intent
)

:confirm_payment_intent
REM Trim any unwanted characters from the PaymentIntent ID (like quotes and spaces)
set payment_intent_id=%payment_intent_id:"=%
set payment_intent_id=%payment_intent_id:~0,29%

echo PaymentIntent ID: %payment_intent_id%

REM Step 3: Confirm the PaymentIntent using the PaymentIntent ID
curl -X POST https://api.stripe.com/v1/payment_intents/%payment_intent_id%/confirm -u sk_test_4eC39HqLyjWDarjtT1zdp7dc: -d payment_method=pm_card_visa

REM Step 4: Retrieve the status of the PaymentIntent
curl -X GET https://api.stripe.com/v1/payment_intents/%payment_intent_id% -u sk_test_4eC39HqLyjWDarjtT1zdp7dc:

REM Cleanup
del response.json

pause
