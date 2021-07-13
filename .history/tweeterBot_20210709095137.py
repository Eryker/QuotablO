import tweepy
import requests
import time
import os

from tweeter_data import CovidData

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)



while True:
    responseData = requests.get("https://api.quotable.io/random")
    mystatus =  str(responseData.json()['content']) 
    author = str(responseData.json()['author'])
    getData = mystatus + "\n" + "\n"+ author
    api.update_status(status=getData)
    time.sleep(50)


# x = 0
# while True: 
 #   hello = 'hello' + str(x)
  #  api.update_status(hello)
   # time.sleep(30.0)


    
# export API_KEY=1TLIE6kDqqNDETtM2eLdgD1Cg
# export API_SECRET=IDc9DwodDZXmOVwIwgGVX8YzoPlkaqcc4nkPuJv4HakfuKd002
# export ACCESS_TOKEN=1402676174644514821-ACUMddhQqgr5mKGRTgyaWMZ4ibhxUs
# export ACCESS_TOKEN_SECRET=YlYWPJY8TACMXlu4bONL4XNrI38cvjJWf4cJTCNmTFCaD