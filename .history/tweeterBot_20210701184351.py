from requests.models import Response
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

def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    Response = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]
  
while True:
    try:
        quote,author = get_Quote()
        status = quote+" -"+author+"\n"+"#python \
        #dailypython #twitterbot #pythonquotes #programming"
        print('\nUpdating : ',status)
        api.update_status(status=status)
        print("\nGoing to Sleep for 1 min")
        time.sleep(60)
    except Exception as ex:
        print(ex)
        break


# x = 0
# while True: 
 #   hello = 'hello' + str(x)
  #  api.update_status(hello)
   # time.sleep(30.0)


    
