from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pywhatkit
from datetime import datetime

# Create a new instance of the Chrome browser
#driver = webdriver.Chrome()

# URL of the webpage with pagination
url = "https://jobs.bdjobs.com/JobSearch.asp?icatId=&requestType=deadline"

# Open the webpage
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find_all('div',id='bottomPagging')
table = soup.find_all('li')
for i in table:    
    
    print(i)


'''
driver.get(url)
# Locate and click the "Next" button or pagination link
next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
next_button.click()

# Wait for a moment for the page to load
time.sleep(10)
'''
