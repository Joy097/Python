from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pywhatkit
from datetime import datetime


driver = webdriver.Chrome()
url = "https://jobs.bdjobs.com/JobSearch.asp?icatId=&requestType=deadline"

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

driver.get(url)  

def next():
        next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
        next_button.click()
        
def make_csv():
        current_time = datetime.now()
        time = current_time.strftime('_%d-%m')
        data = {'Job Title':job_ttl, 'Company':comp, 'Location':loc, 'Education':edu, 'Experience':exp, 'Deadline':date}
        df = pd.DataFrame(data)
        txt = f'bdjobs{time}.csv'
        df.to_csv(txt,index=False,encoding='utf-8')

def send_msg():
        str1=''
        if 'Na' in exp:
                indx=exp.index('Na')
                str1=f'There is a {job_ttl[indx]} job for you with no experience at {comp[indx]} inside {loc[indx]}!!'
        current_time = datetime.now().time()
        hour = int(current_time.strftime('%H'))
        minute = int(current_time.strftime('%M'))
        pywhatkit.sendwhatmsg('+8801959842041','There are many jobs today!'+str1,hour,minute+2)

for i in range(int(lst_pg[3:])):
    current_page_html = driver.page_source
    soup2 = BeautifulSoup(current_page_html,'html')
    table1 = soup2.find_all('div',class_='norm-jobs-wrapper')
    table2 = soup2.find_all('div',class_='sout-jobs-wrapper')
    
    

    for x in table1:
            user = x.find_all('div',class_='col-sm-12')
            names = [head.text.strip() for head in user]
            try:
                edu.append(names[0])
            except IndexError:
                edu.append("None")
            try:
                edu.append(names[1])
            except IndexError:
                edu.append("None")
            try:
                edu.append(names[2])
            except IndexError:
                edu.append("None")
            try:
                edu.append(names[4])
            except IndexError:
                edu.append("None")
            try:
                exp.append(names[-1])
            except IndexError:
                exp.append("None")
            try:
                exp.append(names[5][-11:])
            except IndexError:
                exp.append("None")
        
    for j in table2:
            user = j.find_all('div',class_='col-sm-12')
            names = [head.text.strip() for head in user]
            try:
                edu.append(names[1])
            except IndexError:
                edu.append("None")
            try:
                edu.append(names[2])
            except IndexError:
                edu.append("None")
            try:
                edu.append(names[4])
            except IndexError:
                edu.append("None")
            try:
                edu.append(names[6])
            except IndexError:
                edu.append("None")

            try:
                exp.append(names[-1])
            except IndexError:
                exp.append("None")
            try:
                exp.append(names[-2][-11:])
            except IndexError:
                exp.append("None")

    
    next()
    print(len(job_ttl),len(comp),len(loc),len(),len(),len())
make_csv()

job_ttl=[]
comp = []
loc=[]
edu = []
exp = []
date = []