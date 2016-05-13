## Information
# nei's TwiPNGBot
# This bot is meant to help you upload your PNG image as avatar.
# Go to https://github.com/neistuff/TwiPNGAvatar to get all the information!

## Libraries and informations
# Libraries import
import tweepy
from TwiPNGAvatar import *

# Basic informations
__program__ = "nei's TwiPNGBot"
__version__ = "1.0.0"

## Auth stuff
# My own consumer keys are stocked in a file.
# Bot's auth stuff
keysFile=open("keysBot.txt","r")
keys=keysFile.readlines()
consumer_key=keys[0].rstrip() # .rstrip() gets us rid off of \n
consumer_secret=keys[1]
keysFile.close()
authBot=tweepy.OAuthHandler(consumer_key,consumer_secret) # Just replace them with your own keys.

# Script's auth stuff
authScript=script_auth()

## Stream listener stuff
# This class is the Stream Listener. It is here in order to read EVERY SINGLE TWEET sent in the world in almost real time.
class MyStreamListener(tweepy.StreamListener):
    
    # Sends the tweet it was looking for to the crossFunction
    def on_status(self, status):
        print("This is a placeholder since it is still indev")
    
    # If something happened, it prints an error code.
    def on_error(self, status_code):
        print("Some error occured. Error code : " + str(status_code))
        print("Go to https://dev.twitter.com/overview/api/response-codes to see what it stands for.")
        print("You can also send me a tweet @neistuff and I'll look out for it, that would actually help me. Thanks!")

# Creating a new instance of stream listener and accessing the stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

try:
    # Basically we have to filter all those tweets. Here, we're only looking for those with '@neiHugBot' inside : mentions.
    myStream.filter(track = ['@neipngbot'])
    
# As always, errors can occur.
except AttributeError:
    print("Some error occured. Error code : " + str(status_code))
    print("Go to https://dev.twitter.com/overview/api/response-codes to see what it stands for.")
    print("You can also send me a tweet @neistuff and I'll look out for it, that would actually help me. Thanks!")  