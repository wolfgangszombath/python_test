# List Comprehension
import math

lst = list(range(1,11))
myList = [x*2+1 for x in lst]
print(myList)
myList2dim = [[x, x*x, math.pow(x,3)] for x in lst]
print(myList2dim)

for x in lst:
    print(x, int(math.pow(x,2)), int(math.pow(x,3)), sep='\t')