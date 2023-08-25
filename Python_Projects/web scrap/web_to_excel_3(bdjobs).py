from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://bdjobs.com/career/careercouncil/CareerCounsellingCategory.asp'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all(class_='question-card')

# Create an empty list to store the extracted data
reply_list = []

# Loop through the 'question-card' elements
for part in table[0]:
    if isinstance(part, str):
        reply_list.append(part.strip())  # Append the string content
    else:
        replies = part.find_all('p')
        for reply in replies:
            reply_list.append(reply.get_text(strip=True))

# Create a DataFrame using pandas
df = pd.DataFrame(reply_list, columns=['Replies'])

# Print the DataFrame
print(df)
