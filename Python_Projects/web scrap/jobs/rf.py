from datetime import datetime
import pandas as pd
current_time = datetime.now()
time = current_time.strftime('%Y-%m-%d %H:%M:%S')
data = {'Job Title':'job_ttl', 'Company':'comp', 'Location':'loc', 'Education':'edu', 'Experience':'exp', 'Deadline':'date'}
df = pd.DataFrame(data)
df.to_csv(r'bdjobs{time}.csv',index=False,encoding='utf-8')