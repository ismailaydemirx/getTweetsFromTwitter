import snscrape.modules.twitter as sntwitter
import pandas as pd

# Kullanıcı adları
usernames = ['twitter', 'elonmusk']

# Kaç tweet çekileceği
tweet_count = 50

# Tweetleri bir DataFrame'e ekleme
tweets_list = []
for username in usernames:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+username).get_items()):
        if i >= tweet_count:
            break
        tweets_list.append([tweet.date, tweet.username, tweet.content])
df = pd.DataFrame(tweets_list, columns=['date', 'username', 'tweet'])

# Timezone bilgilerini atma
df['date'] = df['date'].apply(lambda x: x.replace(tzinfo=None))

# Excel dosyasına yazdırma
excel_filename = '_'.join(usernames) + '_tweets.xlsx'
with pd.ExcelWriter(excel_filename) as writer:
    df.to_excel(writer, index=False)

# Başarılı bir şekilde kaç tweet çekildiğini ve hangi hesaplardan çekildiğini yazdırma
print(f"{tweet_count} tweet {', '.join(usernames)} hesaplarından başarılı bir şekilde çekildi.")
