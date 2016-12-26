from flask import Flask, render_template
import os
#import twitterScraper.tweetParser
#import twitterScraper.TwitterListener 
#from twitterScraper.scraper import *
import tweepy
from server import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

#testing
def print_stuff():
	#for status in tweepy.Cursor(api.home_timeline).items(10):
	#	process_or_store(status._json)



if __name__ == "__main__":
	
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)