import pywhatkit
from datetime import datetime
current_time = datetime.now().time()
hour = int(current_time.strftime('%H'))
minute = int(current_time.strftime('%M'))

pywhatkit.sendwhatmsg('+8801959842041','Happy Birthday',hour,minute+1)