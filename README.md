\# Arcade STEM API

This is a simple Flask API for creating Stripe Payment Intents. The API has two endpoints: one for checking the status of the API and another for creating payment intents.

## Endpoints

### Status Endpoint

- **URL:** `/status`
- **Method:** `GET`
- **Description:** Check if the API is running.
- **Response:**
  \```json
  {
    "status": "up",
    "message": "API is running"
  }
  \```

### Create Payment Intent Endpoint

- **URL:** `/payment_intent`
- **Method:** `POST`
- **Description:** Create a Stripe Payment Intent.
- **Request Body:**
  \```json
  {
    "amount": 500,  // Amount in cents (default is 500 cents or $5.00)
    "currency": "usd"  // Currency (default is "usd")
  }
  \```
- **Response:**
  \```json
  {
    "status": "success",
    "client_secret": "your_client_secret"
  }
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

3. **Create a `.env.local` file and add your Stripe API key:**
    \```plaintext
    STRIPE_API_KEY=your_stripe_api_key
    \```

4. **Run the application:**
    \```shell
    python app.py
    \```

### Docker Setup

1. **Build the Docker image:**
    \```shell
    docker build -t arcade-stem-api .
    \```

2. **Run the Docker container:**
    \```shell
    docker run --rm -d -p 5000:5000 --name arcade-stem-container -e STRIPE_API_KEY=your_stripe_api_key arcade-stem-api
    \```

Replace `your_stripe_api_key` with your actual Stripe API key.


## Notes

- Make sure not to expose your Stripe API key publicly.
- This API is intended for educational purposes and should not be used in production without proper security measures.