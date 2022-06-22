#of course u can use any account you want, but this is just for example
import sys 
import tweepy
sys.path.append('../')
from auth import api

user = 'isco_adams'
limit = 40
try:
   tweets = tweepy.Cursor( api.user_timeline,screen_name=user , tweet_mode = 'extended' ).items(limit)
   account_data =[] 
   for tweet in tweets:
      if tweet.full_text.startswith('RT'): #RT means retweeted by someone else
         account_data.append([tweet.user.screen_name,tweet.full_text,tweet.created_at])      
except tweepy.TweepError as e:
   print(e.reason)
   print("Failed to fetch tweets for user:", user)
   sys.exit(1)         
  
"""
//some data u can get from the user
print(user_data)
for friend in user.friends():
   print(friend.screen_name)
"""