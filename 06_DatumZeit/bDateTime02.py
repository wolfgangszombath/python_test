import locale
from datetime import datetime, date

now = datetime.now()
print(now.isoformat())
print(now.strftime('%d.%m.%Y'))
locale.setlocale(locale.LC_ALL, 'de_DE')
print(now.strftime('%A, %d, %B %Y'))
locale.setlocale(locale.LC_ALL, 'it_IT')
print(now.strftime('%A, %d, %B %Y'))
locale.setlocale(locale.LC_ALL, 'fr_FR')
print(now.strftime('%A, %d, %B %Y'))
locale.setlocale(locale.LC_ALL, 'en_US')
print(now.strftime('%A, %d, %B %Y'))

