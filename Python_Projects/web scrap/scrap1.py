from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_titles = [title.text.strip() for title in world_titles]
result=pd.DataFrame(columns=world_titles)
rows = table.find_all('tr')

for row in rows[1:]:
    row_data = row.find_all('td')
    row_data = [list.text.strip() for list in row_data]
    length = len(result)
    result.loc[length] = row_data
result.to_csv(r'C:\\Users\\shiha\\OneDrive\Desktop\\Python-main\\companies.csv',index)