'''
Erweitern Sie das Script aus Abschnitt 8.2, »Beispiel: Schaltjahrtest
«, dahingehend, dass auch die Tage des Monats bestimmt werden.
'''

jahr = int(input("Geben Sie eine Jahreszahl ein\n"))
monat = int(input("Geben Sie die Zahl des Monats an (Jänner = 1, Feber = 2 usw.)\n"))

leapYear = jahr % 400 == 0 or (jahr % 100 != 0 and jahr %4 == 0)

if monat in (1, 3, 5, 7, 8, 10, 12):
  tage = 31
elif monat in (4, 6, 9, 11):
  tage = 30
elif monat == 2:
  tage = 29 if leapYear else 28
else:
  print('Ungültiges Monat!')
  tage = 0

print('Das %d. Monat im Jahr %d hat %d Tage.' 
      % (monat, jahr, tage)) 
                
