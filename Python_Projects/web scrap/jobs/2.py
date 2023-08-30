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

job_ttl=[]
comp = []
loc=[]
edu = []
exp = []
date = []

count=0
driver.get(url)  
for i in range(2):
    current_page_html = driver.page_source
    print(current_page_html)
    table1 = soup.find_all('div',class_='norm-jobs-wrapper')
    table2 = soup.find_all('div',class_='sout-jobs-wrapper')
    
    

    for x in table1:
            user = x.find_all('div',class_='col-sm-12')
            names = [head.text.strip() for head in user]
            job_ttl.append(names[0])
            comp.append(names[1])
            loc.append(names[2])
            edu.append(names[4])
            exp.append(names[-1])
            date.append(names[5][-11:])
            
    for j in table2:
            user = j.find_all('div',class_='col-sm-12')
            names = [head.text.strip() for head in user]
            job_ttl.append(names[1])
            comp.append(names[2])
            loc.append(names[4])
            edu.append(names[6])
            exp.append(names[-1])
            date.append(names[-2][-11:])
        
    
    
    
    next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
    next_button.click()

data = {'Job Title':job_ttl, 'Company':comp, 'Location':loc, 'Education':edu, 'Experience':exp, 'Deadline':date}
df = pd.DataFrame(data)
df.to_csv(r'bdjobs0.csv',index=False,encoding='utf-8')

