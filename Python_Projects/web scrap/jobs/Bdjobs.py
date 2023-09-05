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
        print(txt)
        try:
                df.to_csv(txt,index=False,encoding='utf-8')
                print('done')
        except Exception as e:
                print(str(e))

def send_msg():
        count=0
        for i in exp:
                if i=='Na':
                        count+=1
        current_time = datetime.now().time()
        hour = int(current_time.strftime('%H'))
        minute = int(current_time.strftime('%M'))
        pywhatkit.sendwhatmsg('+8801959842041',f'There are total {count} jobs for you with no experience!!',hour,minute+2)
        
def clean1(list):
        leng = 7-len(list)
        if leng>0:
                for i in range(leng):
                        list.append("null")
        return list

def clean2(list):
        leng = 8-len(list)
        if leng>0:
                for i in range(leng):
                        list.append("null")
        return list
                        

for i in range(int(lst_pg[3:])):
    current_page_html = driver.page_source
    soup2 = BeautifulSoup(current_page_html,'html')
    table1 = soup2.find_all('div',class_='norm-jobs-wrapper')
    table2 = soup2.find_all('div',class_='sout-jobs-wrapper')
    
    try:

        for x in table1:
                user = x.find_all('div',class_='col-sm-12')
                names = [head.text.strip() for head in user]
                names=clean1(names)
                job_ttl.append(names[0])
                comp.append(names[1])
                loc.append(names[2])
                edu.append(names[4])
                exp.append(names[-1])
                date.append(names[5][-11:])
                
        for j in table2:
                user = j.find_all('div',class_='col-sm-12')
                names = [head.text.strip() for head in user]
                names=clean2(names)
                job_ttl.append(names[1])
                comp.append(names[2])
                loc.append(names[4])
                edu.append(names[6])
                exp.append(names[-1])
                date.append(names[-2][-11:])
                
        
                
    except:
            continue
    
    
        
    next()
make_csv()
send_msg()

