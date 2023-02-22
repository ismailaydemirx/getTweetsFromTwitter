import snscrape.modules.twitter as sntwitter
import pandas as pd
import openpyxl
import pytz
from datetime import datetime

query = 'from:elonmusk OR from:twitter'
tweets = []
limits = 10

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limits:
        break
    tweet_date = tweet.date
    if tweet_date.tzinfo is not None:
        tweet_date = tweet_date.astimezone(pytz.utc).replace(tzinfo=None)
    tweets.append([tweet_date, tweet.username, tweet.content + " YourBrand"])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df.to_excel('tweets.xlsx', index=False, sheet_name="TweetsFromBPTHaberAndPusholder")
print(df)