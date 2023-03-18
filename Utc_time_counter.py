import datetime
import pytz
'''

#---------------- datetime.date =>
tday=datetime.date.today()#print today's date
print(tday)
print(tday.year)
print(tday.weekday()) #monday is 0 and sunday is 6
print(tday.isoweekday()) #monday is 1 and sunday is 7
#time delta
tdelta=datetime.timedelta(days=7) #for difference
print(tday+ tdelta) #the date after 7 days 

#difference between dates
bday= datetime.date(2022,8,21)
till_bday=bday-tday
print(till_bday)
#total_seconds
print(till_bday.total_seconds())

#----------------- datetime.time =>
#t= datetime.time(hours,min,sec,microsec)
t= datetime.time(5,47,30,40000)

#-----------------datetime.datetime=>
r=datetime.datetime(2028,3,25,5,33,56,100000)

dt_today = datetime.datetime.today()#without timezone
dt_now = datetime.datetime.now()#can use timezone. but without timezone
dt_utcnow = datetime.datetime.utcnow()#uses time zone
'''
dt=datetime.datetime(2016,7,27,12,30,45,1000, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_dhaka=dt_now.astimezone(pytz.timezone('Asia/Dhaka'))
print(dt_dhaka)
c='July 26, 2022'
a=dt_dhaka.strftime('%B %d, %Y')  # date to string
b=datetime.datetime.strptime(c,'%B %d, %Y') #string to date
print(b)





