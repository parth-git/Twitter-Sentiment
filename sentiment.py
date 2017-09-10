import tweepy
from textblob import TextBlob

consumer_key = '' # Get Key from Twitter dev channel
consumer_secret = ''# Get Key from Twitter dev channel


access_token = '' # Get token from Twitter dev channel
access_token_secret = '' # Get token from Twitter dev channel

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
   
