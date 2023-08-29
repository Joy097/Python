import pywhatkit
from datetime import datetime
current_time = datetime.now().time()
hour = current_time.strftime('%H')
minute = current_time.strftime('%M')

pywhatkit.sendwhatmsg('+8801959842041','Happy Birthday',hour,41)