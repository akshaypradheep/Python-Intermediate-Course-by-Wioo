import datetime
from datetime import timedelta

dt1= input('Enter the first date in YYYY.MM.DD format :')
year, month, day = map(int, dt1.split('.'))
date1 = datetime.date(year, month, day)


dt2= input('Enter the second date in YYYY.MM.DD format :')
year, month, day = map(int, dt2.split('.'))
date2 = datetime.date(year, month, day)


diff=date2-date1
print(diff.days)
