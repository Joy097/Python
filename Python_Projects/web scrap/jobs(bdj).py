from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://jobs.bdjobs.com/JobSearch.asp?icatId=&requestType=deadline"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
print(soup)
table = soup.find_all('div',class_='question-card')
'''
res_names=[]
dates = []
views = []
comments = []
tags = []
titles = []
replies=[]
for i in table:    
    name = i.find_all('ul')
    for j in name:
        user = j.find_all('li')
        names = [head.text.strip() for head in user]
        res_names.append(names[0])
        dates.append(names[1])
        views.append(names[2][:-7])
        comments.append(names[3][:-9])
        tags.append(names[4])
        
        
    text = i.find_all('p')
    text = [psg.text.strip() for psg in text]
    replies.append(text[0])
    
    title = i.find_all('h4')
    text = [psg.text.strip() for psg in title]
    titles.append(text[0])
data = {'Name':res_names, 'Title':titles, 'Reply':replies, 'Date':dates, 'Views':views, 'Comments':comments, 'Tags':tags}
df = pd.DataFrame(data)
df.to_csv(r'C:\\Users\\shiha\\OneDrive\Desktop\\Python-main\\bdjobs2.csv',index=False)
'''