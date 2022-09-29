#mit einer for in range Schleife
from functools import reduce

sum = 0
for i in range(1,10001):
    sum += i
print('Summe der Zahlen von 1 bis 1000:', sum)

#mit einer while Schleife
sum = 0
i = 1
while i <= 10000:
    sum += i
    i += 1
print('Summe der Zahlen von 1 bis 1000:', sum)

sum = reduce(lambda x , y: x +y, list(range(1,1001)))
print('Summe der Zahlen von 1 bis 1000:', sum)

sum = sum(i for i in range(1,1001))
print('Summe der Zahlen von 1 bis 1000:', sum)