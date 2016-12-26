from flask import Flask, render_template, jsonify
import os
#import twitterScraper.tweetParser
#import twitterScraper.TwitterListener 
#from twitterScraper.scraper import *
import tweepy
from server import *
import AlertsRSSFeedScraper.xmlParser
from AlertsRSSFeedScraper.xmlParser import getAllData

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/RSSFeedData', methods = ["GET"])
def getRSSFeed():
	return jsonify(result=getAllData())

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)