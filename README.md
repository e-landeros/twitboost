# TwitBoost

TwitBoost is a micro-SaaS application designed to assist small businesses in generating engaging Twitter content. By using machine learning, it imitates the style of popular Twitter users, helping businesses to align their brand voice with those who inspire them. TwitBoost is built using FastAPI and OpenAI's GPT-4.

## Features

- User authentication via Twitter OAuth.
- Generation of tweet content based on provided Twitter handles.
- Ability to review and select from generated content options.
- Scheduling of posts directly to Twitter.

## Getting Started

### Prerequisites

- Python 3.8 or above.
- A Twitter Developer Account (to obtain API keys).
- An OpenAI account (to obtain API key).

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/e-landeros/twitboost.git
    ```

2. Navigate to the project directory:

    ```
    cd twitboost
    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file at the root of your project directory and add your Twitter and OpenAI API keys:

    ```
    OPENAI_API_KEY=your-openai-api-key
    TWITTER_CONSUMER_KEY=your-twitter-consumer-key
    TWITTER_CONSUMER_SECRET=your-twitter-consumer-secret
    TWITTER_ACCESS_TOKEN=your-twitter-access-token
    TWITTER_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret
    ```

### Running the Application

To start the application, use the following command:

```
uvicorn app.main:app --reload
```

The application will be available at http://

