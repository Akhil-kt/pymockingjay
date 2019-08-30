from authenticate import getKey, getSecret
import tweepy

auth = tweepy.OAuthHandler(getKey(), getSecret())

api = tweepy.API(auth)