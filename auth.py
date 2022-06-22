import tweepy
import os
from dotenv import load_dotenv

#accessing tokens and token-secrets
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#authentication
auth = tweepy.OAuth1UserHandler(
   api_key, api_secret, access_token, access_token_secret
)
api = tweepy.API(auth) 
