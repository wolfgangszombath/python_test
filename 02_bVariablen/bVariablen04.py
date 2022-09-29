import copy

c= [1,2,[3,4]]
for var in c:
    print(var)
d = copy.copy(c)
print("c=",c,"\nd=",d)
c[2][0] = 8
print("######## copy.copy #######")
print("c=",c,"\nd=",d)
d = copy.deepcopy(c)
c[2][0] = 5
print("######## copy.deepcopy #######")
print("c=",c,"\nd=",d)
