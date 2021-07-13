import requests
from datetime import datetime, timedelta
import json

class CovidData(): 

 Covid_data = requests.get("https://coronavirusapi-france.vercel.app/FranceLiveGlobalData")

 

 @classmethod
 def GetDate(cls):
     return (CovidData.Covid_data["date"])
            
