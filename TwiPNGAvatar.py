# nei's TwiPNGAvatar.py
# Script that allows you to manually upload your avatar in PNG on Twitter.
# It is meant to work independently of @neipngbot, therefore is the bot is down for some reason, you can still upload your avatar.

# Library import
import tweepy

# Auth stuff
# My own consumer keys are stocked in a file.
def script_auth():
    keysFile=open("keysScript.txt","r")
    keys=keysFile.readlines()
    consumer_key=keys[0].rstrip() # .rstrip() gets us rid off of \n
    consumer_secret=keys[1]
    keysFile.close()
    authScript=tweepy.OAuthHandler(consumer_key,consumer_secret) # Just replace them with your own keys.
    return authScript

authScript=script_auth()

# Grab the url
def get_url(auth):
    print("Go there and paste the PIN :")
    url = auth.get_authorization_url()
    return url

# Grab the pin
def get_pin(auth):
    pin = str(input("PIN: "))

    # GET THE TOKEN
    authScript.get_access_token(pin)
    print("Token gotten ! Launching...")
    
    api = tweepy.API(auth)
    return api

url=get_url(authScript)
print(url)

apiUploader = get_pin(authScript)

# Gets the path of the image, uploads it, and prints a confirmation message.
def change_avatar(api):
    path=input("Name of the image: ")
    api.update_profile_image("./"+path)

change_avatar(apiUploader)    
print("Avatar changed! Press Enter to leave.")
input()
