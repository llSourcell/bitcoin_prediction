# import tweepy library for twitter api access and textblob libary for sentiment analysis
import csv
import tweepy
import numpy as np
from textblob import TextBlob
import datetime
import time

def main():

    # set twitter api credentials
    consumer_key= 'MOe623rxcqck6x8y5XhzK8MJT'
    consumer_secret= 'mcBq9Km1f3OYERRD6vKmOfWSgCjsqzXAreIsn8klxAtPIo40E7'
    access_token='913787859630460928-RXF8NVN3gGbxD64NCZ7wBma5M2WPwlv'
    access_token_secret='P4UU9I2DimdnUown2EM6p4WZ0ftdPNsysDNW6xGh0Ts4f'

    # set path of csv file to save sentiment stats
    path = 'live_tweet.csv'
    f = open(path,"a")
    f1 = open('tweet_data','a')
    # access twitter api via tweepy methods
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth)

    while True:

        # fetch tweets by keywords
        tweets = twitter_api.search(q=['bitcoin, price, crypto'], count=100)

        # get polarity
        polarity = get_polarity(tweets,f1)
        sentiment = np.mean(polarity)

        # save sentiment data to csv file
        f.write(str(sentiment))
        f.write(","+datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
        f.write("\n")
        f.flush()
        time.sleep(60)
    

def get_polarity(tweets,f):
    # run polarity analysis on tweets

    tweet_polarity = []

    for tweet in tweets:
        f.write(tweet.text+'\n')
        analysis = TextBlob(tweet.text)
        tweet_polarity.append(analysis.sentiment.polarity)

    return tweet_polarity

main()
