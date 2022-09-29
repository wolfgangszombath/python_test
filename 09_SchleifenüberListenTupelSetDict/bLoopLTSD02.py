import math

lst = [1,2,3,7,11,13,19, 23]
result = [x*x for x in lst]
print (result)
# nur gerade Zahlen berücksichtigen
result2 = [ math.pow(x,2) for x in lst if x%2 == 0]
print(result2)

# Ausgabe in eine Liste
result3 = [[x, x*x] for x in lst]
print(result3)

dict = {x:x*x for x in lst}
print(dict)