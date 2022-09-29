myFirstNumber = input("Geben Sie eine ganze Zahl ein\n")
mySecNumber = input("Geben Sie noch eine ganze Zahl ein\n")

#Die verschiedenen Divisionsarten
#normale Division
result = float(myFirstNumber) / float(mySecNumber)
print(result)
#Ganzzahldivision gerundet
roundDigits = int(input("Geben Sie bitte die Zahl der Stellen nach dem Komma ein"))
result = round(result,roundDigits)
#Ganzzahldivision
result = float(myFirstNumber) // float(mySecNumber)
print(result)
#Modulodivision
result = int(myFirstNumber) %  int(mySecNumber)
print(result)
