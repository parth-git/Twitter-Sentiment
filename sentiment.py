import tweepy
from textblob import TextBlob

consumer_key = 'fluo93m7MbQTQWWkUoJjeLkwW'
consumer_secret = 'klOSEAkK3yARMk8TQw6n2JQgtiVxDZB6Moq7OcvIlOGlV5McE5'


access_token = '363464909-hkMIzgJ5xz6IhbT2lOsDTCqac07vn9C01XLZ8UUm'
access_token_secret = '8IMTD6Ua3Kf4DLYq93GRJdJkoyeSiQhDn4V5zrl4KLsBu'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
   