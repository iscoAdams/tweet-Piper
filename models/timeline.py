import sys 
sys.path.append('../')
from auth import api
import tweepy
limit = 40
try:
    tweets = tweepy.Cursor( api.home_timeline, tweet_mode = 'extended' ).items(limit)
    public_tweets =[] 
    for tweet in tweets:
          public_tweets.append([tweet.user.screen_name,tweet.full_text,tweet.created_at]) 
except tweepy.TweepError as e:
    print(e.reason)
    print("Failed to fetch tweets")
    sys.exit(1)          
# for tweet in public_tweets:
    # print(tweet.text) 