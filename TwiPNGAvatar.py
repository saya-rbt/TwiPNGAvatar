# nei's TwiPNGAvatar.py

# Library import
import tweepy

# Auth stuff
auth=tweepy.OAuthHandler("3wv3VFOZkEH1QVCfd0KHljKXV","15WqohzK9TDYgxIr4WTxLeJb32lO5q7IMfjjM0IbqntcJaVjcG")

# Grab the pin
print("Go there and paste the PIN :")
url = auth.get_authorization_url()
print(url)
pin = input("PIN: ")

# GET THE TOKEN
auth.get_access_token(pin)
print("Token gotten ! Launching...")

api = tweepy.API(auth)

# Gets the path of the image, uploads it, and prints a confirmation message.
path=input("Name of the image: ")
api.update_profile_image(path)
print("PP changed!")
