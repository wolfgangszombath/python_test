from datetime import datetime
x = 1
now = datetime.now()
print(now)
print(now.time())
start = now.timestamp()
for i in range(10000000):
    x = x**x
end = datetime.now().timestamp()
dur = end - start
print("Dauer:" + str(round(dur,3)))

