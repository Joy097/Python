from bs4 import BeautifulSoup
import requests
import pandas as pd



url = f"https://checkpagerank.net/check-page-rank.php"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
