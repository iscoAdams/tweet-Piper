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
try:
   auth = tweepy.OAuth1UserHandler(
   api_key, 
   api_secret, 
   access_token,
   access_token_secret
   )
except tweepy.TweepError as e:
   print(e)
   exit()   
api = tweepy.API(auth, wait_on_rate_limit=True)