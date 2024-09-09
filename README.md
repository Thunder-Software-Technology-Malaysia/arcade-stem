# Arcade STEM API

This is a simple Flask API for creating Stripe Payment links, and handling Stripe webhooks. The API has several endpoints, including one for checking the status of the API, creating payment links, and handling webhooks.

## Endpoints

### Status Endpoint

### Create Payment Link Endpoint

- **URL:** `/create-payment-link`
- **Method:** `POST`
- **Description:** Create a Stripe Payment Link with optional machine metadata.
- **Request Body:**
  \```json
  {
    "machine_id": "unique_machine_id"  // Optional machine ID to track the payment
  }
  \```
- **Response:**
  \```json
  {
    "url": "https://payment-link.url"  // URL to the payment link
  }
  \```

- **Testing with `curl`:**
  - You can test the `/create-payment-link` endpoint using the following `curl` command:
    \```shell
    curl -X POST http://localhost:5000/create-payment-link -H "Content-Type: application/json" -d "{\"machine_id\":\"machine_123\"}"
    \```

### Stripe Webhook Endpoint

- **URL:** `/webhook`
- **Method:** `POST`
- **Description:** Stripe webhook to handle events such as payment completions.
- **Request Body:** Stripe sends the event payload automatically.
- **Response:**
  \```plaintext
  200 OK on success, 400 for validation errors
  \```

- **Event Handling:** The webhook listens for the `checkout.session.completed` event, verifies the event signature, and updates the status of the machine if `machine_id` is provided in the metadata.

- **Testing Webhooks with Stripe CLI:**
  - You can forward Stripe events to your local webhook using the following Stripe CLI command:
    \```shell
    stripe listen --forward-to localhost:5000/webhook
    \```

## Running the API

### Prerequisites

- Python 3.6 or higher
- Flask
- Stripe
- python-dotenv

### Local Setup

1. **Clone the repository:**
    \```shell
    git clone https://github.com/Thunder-Software-Technology-Malaysia/arcade-stem.git
    cd arcade-stem-api
    \```

2. **Install dependencies:**
    \```shell
    pip install -r requirements.txt
    \```

3. **Create a `.env.local` file and add your Stripe API key and Webhook secret:**
    \```plaintext
    STRIPE_API_KEY=your_stripe_api_key
    STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
    \```

4. **Run the application:**
    \```shell
    python app.py
    \```

### Docker Setup

\> **Note:** The current Docker setup does not support the new `/create-payment-link` and `/webhook` endpoints. Support for these will be added in a future update.

1. **Build the Docker image:**
    \```shell
    docker build -t arcade-stem-api .
    \```

2. **Run the Docker container:**
    \```shell
    docker run --rm -d -p 5000:5000 --name arcade-stem-container -e STRIPE_API_KEY=your_stripe_api_key arcade-stem-api
    \```

Replace `your_stripe_api_key` with your actual Stripe API key.

## Example Docker Command

\```shell
docker run --rm -d -p 5000:5000 --name arcade-stem-container -e STRIPE_API_KEY=your_stripe_api_key arcade-stem-api
\```

Replace `your_stripe_api_key` with your actual Stripe API key.

## Stripe CLI Setup on Windows (Without Scoop)

To install the Stripe CLI on Windows without using Scoop:

1. **Download the latest** `windows` **zip file** from [GitHub](https://github.com/stripe/stripe-cli/releases).
 
2. **Unzip the** `stripe_X.X.X_windows_x86_64.zip` **file.**

3. **Add the path to the unzipped** `stripe.exe` **file to your** `Path` **environment variable.** To learn how to update environment variables, see the [Microsoft PowerShell documentation](https://docs.microsoft.com/en-us/powershell/scripting/setup/environment-variables?view=powershell-7.1).

> **Note:** Windows anti-virus scanners occasionally flag the Stripe CLI as unsafe. This is very likely a false positive. For more information, see [issue #692](https://github.com/stripe/stripe-cli/issues/692) in the GitHub repository.

## Notes

- Make sure not to expose your Stripe API key and webhook secret publicly.
- This API is intended for educational purposes and should not be used in production without proper security measures.