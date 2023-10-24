from bs4 import BeautifulSoup
import requests
import pandas as pd



url = f"https://siterankdata.com/{site}"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('h1')[1]
hlist = [head.text.strip() for head in table]
