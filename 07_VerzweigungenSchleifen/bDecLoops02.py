tag = 3
if tag == 1:
    s = "Montag"
elif tag == 2:
    s = "Dienstag"
elif tag == 3:
    s = "Mittwoch"
elif tag == 4:
    s = "Donnerstag"
elif tag == 5:
    s = "Freitag"
elif tag == 6:
    s = "Samstag"
else:
    s = "Sonntag"


print(str(tag) + ": " + s)
#Nutzung eines Dictionarys
tag = int(input("Geben Sie einen Wochentag (1 -7) ein\n"))
alletage = {
    1: 'Montag',
    2: 'Dienstag',
    3: 'Mittwoch',
    4: 'Donnerstag',
    5: 'Freitag',
    6: 'Samstag',
    7: 'Sonntag'}
if tag in alletage:
    s = alletage[tag]
else:
    s = 'ungültig';
print(str(tag) + ": " + s)

