from datetime import datetime
current_time = datetime.now().time()
time = current_time.strftime('%Y-%m-%d %H:%M:%S')
print(time)