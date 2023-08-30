from datetime import datetime
import pandas as pd
job_ttl=[]
comp = []
loc=[]
edu = []
exp = []
date = []
current_time = datetime.now()
time = current_time.strftime('%d-%m_%H:%M')
data = {'Job Title':job_ttl, 'Company':comp, 'Location':loc, 'Education':edu, 'Experience':exp, 'Deadline':date}
df = pd.DataFrame(data)
txt = f'bdjobs{time}.csv'
df.to_csv(txt,index=False,encoding='utf-8')