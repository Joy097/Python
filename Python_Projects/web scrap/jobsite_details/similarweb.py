from bs4 import BeautifulSoup
import requests
import pandas as pd



url = f"https://www.similarweb.com/website/bdjobs.com/#overview"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
