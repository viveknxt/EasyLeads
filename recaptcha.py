SITE_URL = "https://dashboard.easyleadz.com/elogin"
SITE_KEY = "6LdZ2ygTAAAAABH_7I9mj2AvLYbr6SXbq3sMbcH2"


import os
import sys
import time

import requests
from twocaptcha import TwoCaptcha
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method


MY_API_KEY = os.environ.get('API_KEY')

def captcharesolver():
    solver = TwoCaptcha(MY_API_KEY)

    try:
        result = solver.resolve_captcha(
            site_key=SITE_KEY,
            page_url=SITE_URL)
    except Exception as e:
        sys.exit(e)
    else:
        response_site = requests.get("https://dashboard.easyleadz.com/elogin")
        # print(response_site.text)
        


        url = "http://2captcha.com/in.php"
        response = requests.get(
            url, params= {"key": os.environ.get("API_KEY"), 
                            "method": "userrecaptcha", 
                            "googlekey": SITE_KEY, 
                            "pageurl": SITE_URL})
        print(response.text)
        time.sleep(15)

        # url2 = "http://2captcha.com/res.php" 

        # req_sol = requests.get(url2, params={'key': MY_API_KEY, 'action': 'get', 'id':response})
        # print(req_sol.text)