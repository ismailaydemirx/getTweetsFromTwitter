import snscrape.modules.twitter as sntwitter
import pandas as pd
import openpyxl

query= "(from:elonmusk)"
tweets=[]
limits=30
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets)==limits:
        break
    tweets.append([tweet.date,tweet.username, tweet.content])

df = pd.DataFrame(tweets,columns=['Date','User','Tweet'])
print(df)
