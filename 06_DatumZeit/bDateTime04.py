from datetime import date , datetime , timedelta
today = datetime.now().date() # date
week = timedelta(weeks=1) # timedelta
print(today , today + week , today + 3 * week)

now = datetime.now() # datetime
minute = timedelta(minutes=1) # timedelta
soon = now + 10 * minute # datetime
print(now.time(), soon.time())

# Beispielprogramm measure.py
import time , math
start = time.process_time()
# sinnlos Zeit totschlagen
for i in range(1, 10000000):
    x=math.sin(i)
end = time.process_time()
print(end - start , 'Sekunden')