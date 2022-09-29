jahr = int(input("Geben Sie eine Jahreszahl ein"))
schaltjahr = True if ((jahr % 400 == 0 ) or (jahr % 4 == 0 and jahr % 100 != 0)) else False
print(str(jahr) + ': ' + str(schaltjahr))