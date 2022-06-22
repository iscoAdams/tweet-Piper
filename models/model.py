from others import random_tweets
from timeline import public_tweets
from account import account_data
from time import sleep
import pandas as pd

# for account data
account_coloums = ['user','tweet','created_at']
df1 = pd.DataFrame(account_data,columns=account_coloums)
df1.to_csv('../csv-models/account_data.csv',index=True)



#for public tweets
public_coloums = ['user','tweet','created_at']
df2 = pd.DataFrame(public_tweets,columns=public_coloums)
df2.to_csv('../csv-models/public_tweets.csv',index=True)


# for random tweets based on a keyword
random_coloums = ['user','tweet','created_at']
df3 = pd.DataFrame(random_tweets,columns=random_coloums)
df3.to_csv('../csv-models/random_tweets.csv',index=True)
