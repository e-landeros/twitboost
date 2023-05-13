# main.py
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import openai
import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

openai.api_key = os.getenv('OPENAI_API_KEY')

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class Handle(BaseModel):
    handle: str

@app.post("/generate_content/")
def generate_content(handle: Handle):
    # Fetch recent tweets from the given handle
    tweets = api.user_timeline(screen_name=handle.handle, count=10, tweet_mode="extended")
    recent_tweets = " ".join([tweet.full_text for tweet in tweets])

    # Generate new content based on these tweets
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=recent_tweets,
        temperature=0.5,
        max_tokens=280
    )
    return response.choices[0].text.strip()
