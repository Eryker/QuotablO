import tweepy
import time
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
#responseData = requests.get("https://api.quotable.io/random")
#statusText = str(responseData.json['content'])



#while True:
 #  api.update_status(status=statusText)
  # time.sleep(10.0)
x = 0
while True: 
    hello = 'hello'
  #  api.update_status(hello)
   # x+=1
    #time.sleep(10.0)


    