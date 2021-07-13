import tweepy
import requests
import time
import json
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

  def get_Quote():
        params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]



    responseData = requests.get("https://api.quotable.io/random")
    mystatus =  str(responseData.json()['content']) 
    api.update_status(status=mystatus)
    time.sleep(50.0)


# x = 0
# while True: 
 #   hello = 'hello' + str(x)
  #  api.update_status(hello)
   # time.sleep(30.0)


    
