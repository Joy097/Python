from bs4 import BeautifulSoup
import requests
import pandas as pd


def site_rank(site):
    try:
        url = f"https://siterankdata.com/{site}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all('h1')[1]
        hlist = [head.text.strip() for head in table]
        return hlist[0]
    except IndexError:
        return 'N/A'
 
file_path = 'sites.txt' 
data = []

with open(file_path, 'r') as file:
    for line in file:
        site_name = line.strip()
        rank = site_rank(site_name)
        ##add more scrappers here
        data.append([site_name, rank])

    
header = ['Site','Rank']
df = pd.DataFrame(data, columns=header)
df.to_csv(r'C:\\Users\\shiha\\OneDrive\\Desktop\\Office\\Automation\\site_rank_report.csv',index=False)