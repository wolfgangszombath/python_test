import time
from datetime import datetime, date

today = datetime.now()
print(today)
print(today.strftime('%d.%m.'))

now = today.time()
hours = now.hour
minutes = now.minute
secs = now.second
secsSinceMidnight = hours * 3600 + minutes * 60 + secs
print(secsSinceMidnight)

seconds_since_midnight = (today - today.replace(hour=0, minute = 0, second = 0)).total_seconds()
print(seconds_since_midnight)

days_since_newYear = (today - today.replace(day=1, month = 1))
print(days_since_newYear)