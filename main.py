# Constants 
CHROME_DRIVER = "E:\\EasyLeads\\chromedriver"
SITE_URL = "https://dashboard.easyleadz.com/elogin"
SITE_KEY = "6LdZ2ygTAAAAABH_7I9mj2AvLYbr6SXbq3sMbcH2"

# Standard Libraries
import os
import time

# Local Libraries 
from recaptcha import captcharesolver

# Third Party Libraries
import pandas as pd
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method
my_email = os.environ.get('USER_EMAIL')
my_password = os.environ.get('USER_PASS')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dashboard.easyleadz.com/elogin")
email_input = driver.find_element(by='id', value='emailId')
password_input = driver.find_element(By.ID, "passwrd")


email_input.send_keys(my_email)
password_input.send_keys(my_password)



if WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
    (By.CSS_SELECTOR,"iframe[title='reCAPTCHA']"))) == True:
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    #     (By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
    captcharesolver()
else:
    os.exit()
    # myButton = driver.find_element(By.CSS_SELECTOR, ".btn-primary" )
    # myButton.click()


time.sleep(10)

# driver.quit()

