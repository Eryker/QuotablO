import requests
from datetime import datetime, timedelta
import json

class CovidData(): 

 Covid_data = requests.get("https://coronavirusapi-france.vercel.app/FranceLiveGlobalData")

 @classmethod
    def get_today_date(cls):
        return datetime.now().strftime("%Y-%m-%d")
