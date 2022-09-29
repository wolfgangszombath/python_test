# Python erkennt gewisse Datentypen von selbst
iZahl = 3.9 # Ganzzahl int
fZahl  = 3.0 # Fließkommazahl
cZahl = 3 + 4j # komplexe Zahl
isTrue = bool(True) # boolsche Werte
isFalse = bool(False) # boolsche Werte
print(isTrue, type(isTrue))
print(isFalse)
print("fZahl ist vom Typ: ",type(fZahl))
print('Integer' if isinstance(iZahl, int) else 'kein Integer')# Hier wird ein ternärer Operator verwendet!
myIntZahl : int = 12
msg : str = "Wichtige Nachricht"
print(msg, type(msg))
msg = 100
print(msg, type(msg))
print(myIntZahl,'\n' + str(msg))
# Diese Zuweisungen sind aber nicht zwingend
msg = 1
print(msg)