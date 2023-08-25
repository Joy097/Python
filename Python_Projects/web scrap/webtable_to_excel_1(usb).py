from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/US-Bangla_Airlines"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find_all('table')[2]
th = table.find_all('th')

