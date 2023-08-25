from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/US-Bangla_Airlines"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find_all('table')[2]
header = table.find_all('th')
hlist = [head.text.strip() for head in header]
daf = pd.DataFrame(columns=hlist)
#print(daf)

rows = table.find_all('tr')
for row in rows:
    elements = row.find_all('td')
    elist = [elem.text.strip() for elem in elements]
    length = len(daf)
    daf.loc[length]=elist
print(daf)