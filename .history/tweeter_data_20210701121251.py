import requests
from datetime import datetime, timedelta
import json

class CovidData(): 

 Covid_data = requests.get("https://coronavirusapi-france.vercel.app/FranceLiveGlobalData")

 
   #@classmethod
    #def get_daily_first_vaccine_injection(cls):
       # return RozierGuillaumeAPI.vaccine_data["n_dose1"][RozierGuillaumeAPI.get_last_position_vaccine_data()[0]]
            
 @classmethod
 def GetDate(args):
     return CovidData.Covid_data["date"]
     