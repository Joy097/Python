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
driver = webdriver.Chrome()

# URL of the webpage with pagination
url = "https://jobs.bdjobs.com/JobSearch.asp?icatId=&requestType=deadline"

# Open the webpage
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find('div',id='bottomPagging')
table = table.find_all('li')
lst_pg = (i.text.strip() for i in table[5:]).__next__()  


count=0
driver.get(url)  
for i in range(int(lst_pg[3:])):
    current_page_url = driver.current_url
    current_page_html = driver.page_source
    with open(f'file{count}.txt', "w") as file:
    # Write the value into the file
        file.write()
    print(current_page_html)
    # Locate and click the "Next" button or pagination link
    next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
    next_button.click()

    # Wait for a moment for the page to load
    time.sleep(10)
    count+=1

