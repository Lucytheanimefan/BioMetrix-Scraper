import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
import TwitterListener

# set up
consumer_key = 'O9eiLjL4S0eCI7XA0BlcQtqVr'
consumer_secret = 'MBTFnYcxVZxMytBeqg10fF4aJq2m5tfviS601DqMP4H1gu1Ssx'
access_token = '1486245986-krcF4UXvRrR3BrYWDUbHMRAT6Pj5scSd9EXxWV4'
access_secret = 'hoOtgteqiJvp68NO57f37Letwi2mw98aVg58KgbWzlBiz'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# set up stream
twitter_stream = Stream(auth, TwitterListener())
twitter_stream.filter(track=['#anime'])

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)

