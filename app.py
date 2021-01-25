from settings import api_key, api_key_secret, access_token, access_token_secret, bearer_token
import tweepy
import logging
import json
import time

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api.verify_credentials()

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            #api.retweet(status.id)
            #api.create_favorite(status.id)
            print('like and retweeted ' + status.text)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            exit
    def on_error(self, status_code):
        if status_code == 420:
            return False
    
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['dalit', 'adivasi', 'lgbt'], is_async=True)