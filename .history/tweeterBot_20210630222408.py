import tweepy
import requests
import time
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

api = "https://api.quotable.io/random"

while True:
    responseData = str(requests.get(api).json())
    content = responseData['content']
    author = responseData['author']
    mystatus = content + author

    api.update_status(status=mystatus)
    time.sleep(30.0)


# x = 0
# while True: 
 #   hello = 'hello' + str(x)
  #  api.update_status(hello)
   # time.sleep(30.0)


    
