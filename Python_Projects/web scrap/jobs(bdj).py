from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://jobs.bdjobs.com/JobSearch.asp?icatId=&requestType=deadline"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
table = soup.find_all('div',class_='norm-jobs-wrapper')

job_ttl=[]
comp = []
loc=[]
edu = []
exp = []
date = []
for j in table[:5]:
        user = j.find_all('div',class_='col-sm-12')
        names = [head.text.strip() for head in user]
        job_ttl.append(names[0])
        comp.append(names[1])
        loc.append(names[2])
        edu.append(names[4])
        exp.append(names[6])
        date.append(names[5][-11:])
        
length=len(date)

excel_writer = pd.ExcelWriter('unicode_dataframe.xlsx', engine='openpyxl')
df.to_excel(excel_writer, index=False, sheet_name='Sheet1')


'''
data = {'Job Title':job_ttl, 'Company':comp, 'Location':loc, 'Education':edu, 'Experience':exp, 'Deadline':date}
df = pd.DataFrame(data)
df.to_csv(r'bdjobs0.csv',index=False)



with open("file.txt", "w", encoding="utf-8") as file:
            file.write(names[0])
            


data = {'Name':res_names, 'Title':titles, 'Reply':replies, 'Date':dates, 'Views':views, 'Comments':comments, 'Tags':tags}
df = pd.DataFrame(data)
df.to_csv(r'C:\\Users\\shiha\\OneDrive\Desktop\\Python-main\\bdjobs2.csv',index=False)
'''