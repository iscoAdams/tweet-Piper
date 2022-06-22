import sys 
import tweepy
sys.path.append('../')
from auth import api
search_query = 'technews --filter:retweets'
limit = 40
try:
    tweets = tweepy.Cursor( api.search_tweets, q=search_query, lang ='en', tweet_mode = 'extended' ).items(limit)
    random_tweets =[] 
    for tweet in tweets:
          random_tweets.append([tweet.user.screen_name,tweet.full_text,tweet.created_at])      
except tweepy.TweepError as e:
    print(e.reason)
    print("Failed to fetch tweets")
    sys.exit(1)   

# print("Total Tweets fetched:", len(tweets))           
# for tweet in random_tweets:
#     print(tweet)
    
