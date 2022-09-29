list = [1,2,3,4,5,6,7,8,9]
for i in list:
    print(i)
print(i)
lowerLimit = int(input("Untere Grenze?\n"))
upperLimit = int(input("Obere Grenze?\n "))
step = int(input("Schrittweite?\n"))
for i in range (lowerLimit, upperLimit+1, step):
    print(i, i*i)

for ch in 'äöüabc':
    print(ch)
