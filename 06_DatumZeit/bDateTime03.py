import locale
from datetime import date, datetime

today = date.today()
print(today)
locale.setlocale(locale.LC_ALL, 'de_DE')
print(today.strftime('%A, %d. %B %Y'))

print(datetime.now().time())
today = date.today()
clock = datetime.now().time()
together = datetime.combine(today, clock)
print(together)

myYear = int(input("Geben Sie das Jahr ein\n"))
myMonth = int(input("Geben Sie das Monat ein\n"))
myDay = int(input("Geben Sie den Tag ein\n"))
myHours = 0
myMinutes = 0
mySeconds = 0
somedate = datetime(myYear, myMonth, myDay)
print(somedate.strftime('%A, %d. %B %Y'))