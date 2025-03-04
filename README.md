# Get Tweets from Twitter

This script allows you to fetch tweets from specified Twitter accounts without the need for authentication or login. Using the **snscrape** and **pandas** libraries, you can retrieve an unlimited number of tweets from the accounts of your choice and save them to an Excel file for analysis or further processing.

## Requirements

- **snscrape**: A Python library to scrape data from social media platforms like Twitter.
- **pandas**: A powerful data manipulation and analysis library in Python.

## Script Overview

The script scrapes tweets from specified Twitter accounts, storing the tweet's date, username, and content in a pandas DataFrame. The data is then saved to an Excel file for further use.

### Code:

```python
import snscrape.modules.twitter as sntwitter
import pandas as pd

# List of usernames to scrape tweets from
usernames = ['twitter', 'elonmusk']

# Number of tweets to scrape per username
tweet_count = 50

# Scrape tweets and store them in a DataFrame
tweets_list = []
for username in usernames:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + username).get_items()):
        if i >= tweet_count:
            break
        tweets_list.append([tweet.date, tweet.username, tweet.content])
df = pd.DataFrame(tweets_list, columns=['date', 'username', 'tweet'])

# Remove timezone information from the 'date' column
df['date'] = df['date'].apply(lambda x: x.replace(tzinfo=None))

# Save the data to an Excel file
excel_filename = '_'.join(usernames) + '_tweets.xlsx'
with pd.ExcelWriter(excel_filename) as writer:
    df.to_excel(writer, index=False)

# Print a success message with the number of tweets scraped
print(f"{tweet_count} tweets successfully scraped from the following accounts: {', '.join(usernames)}.")
```

### How It Works:

1. **Define Usernames**: The script scrapes tweets from a list of usernames (e.g., `'twitter'`, `'elonmusk'`).
2. **Specify Tweet Count**: Define how many tweets you want to fetch per account.
3. **Data Collection**: It iterates over the list of usernames and scrapes the tweets using `snscrape`.
4. **Data Storage**: The collected data (tweet date, username, and content) is stored in a pandas DataFrame.
5. **Timezone Removal**: Any timezone information is stripped from the timestamp.
6. **Export to Excel**: The data is written to an Excel file with a name based on the usernames scraped.
7. **Success Message**: A confirmation message is printed to inform the user of how many tweets were successfully scraped.

## Output

- The tweets are saved in an Excel file (`_tweets.xlsx`).
- The output will include a summary message indicating the number of tweets successfully retrieved.

---

This script provides a simple way to scrape and save tweets from multiple Twitter accounts for analysis purposes.

---
