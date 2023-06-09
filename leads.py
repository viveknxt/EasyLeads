LEADS_SITE = "https://dashboard.easyleadz.com/search"


import requests
from bs4 import BeautifulSoup


def getlead():
    response = requests.get(LEADS_SITE)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
   
    
getlead()