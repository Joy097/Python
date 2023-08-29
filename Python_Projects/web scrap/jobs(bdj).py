from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://jobs.bdjobs.com/JobSearch.asp?icatId=&requestType=deadline"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find_all('div',class_='norm-jobs-wrapper')

job_ttl=[]
comp = []
loc=[]
edu = []
exp = []
date = []
for j in table[:5]:
        user = j.find_all('div',class_='col-sm-12')
        names = [head.text.strip() for head in user]
        job_ttl.append(names[0])
        comp.append(names[1])
        loc.append(names[2])
        edu.append(names[4])
        exp.append(names[6])
        date.append(names[5][:])
        
print(job_ttl)


'''
with open("file.txt", "w", encoding="utf-8") as file:
            file.write(names[0])
            
job_ttl=[]
comp = []
loc=[]
edu = []
exp = []
date = []
for i in table:    
    name = i.find_all('ul')
    for j in name:
        user = j.find_all('li')
        names = [head.text.strip() for head in user]

        
        
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