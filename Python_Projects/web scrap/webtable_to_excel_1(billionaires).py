from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find_all('table')[2]
header = table.find_all('th')
hlist = [head.text.strip() for head in header]
daf = pd.DataFrame(columns=hlist)
print(daf)
rows = table.find_all('tr')

for row in rows[1:]:
    elements = row.find_all('td')
    elist = [elem.text.strip() for elem in elements]
    length = len(daf)
    daf.loc[length]=elist
print(daf)
daf.to_csv(r'C:\\Users\\shiha\\OneDrive\Desktop\\Python-main\\billionares.csv',index=False)