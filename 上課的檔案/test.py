import datetime
import time

date1="2022-06-14"
date2='2022-05-14'

dateA=time.strptime(date1,'%Y-%m-%d')
dateB=time.strptime(date2,'%Y-%m-%d')

print(dateA)
print(dateB)

now=str(datetime.datetime.now())[:19]
print(now)