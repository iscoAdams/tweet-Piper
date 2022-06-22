from auth import api

public_tweets = api.home_timeline() #list of tweets from my timeline
for tweet in public_tweets:
    print(tweet.text) 