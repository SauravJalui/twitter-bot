import tweepy
import time

consumer_key = '' 
consumer_secret = '' 
access_token = '' 
access_token_secret = '' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "#100daysofcode"
numberoftweets = 500

for tweet in tweepy.Cursor(api.search, search).items(numberoftweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
