from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
#print(soup)
#print("----------------------------------------------------------------")
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_titles = [title.text.strip() for title in world_titles]
print(world_titles)

result=pd.DataFrame(columns=world_titles)
result