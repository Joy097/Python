from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://bdjobs.com/career/careercouncil/CareerCounsellingCategory.asp"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find('div',class_='question-card')
info = table.find_all('ul')
names=[]
for i in info:    
    name = i.find_all('li')[0]
    name = [head.text.strip() for head in name]
    names.append(name[-1])
#hlist = [head.text.strip() for head in header]
#daf = pd.DataFrame(columns=hlist)
print(names)

'''
rows = table.find_all('tr')

for row in rows[1:]:
    elements = row.find_all('td')
    elist = [elem.text.strip() for elem in elements]
    length = len(daf)
    daf.loc[length]=elist
print(daf)
daf.to_csv(r'C:\\Users\\shiha\\OneDrive\Desktop\\Python-main\\billionares.csv',index=False)
'''