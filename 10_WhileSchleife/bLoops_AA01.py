# Das 1 x 1!
#Mit einer for Schleife
for i in range (1,11):
    for j in range(1,11):
        print( '%3dx%3d=%3d\t' % (i,j,i*j), end="")
    print()
print(120*"#")
# Mit einer while in Schleife
i = 1
while i<= 10:
    j = 1
    while j <= 10:
        print('%3dx%3d=%3d\t' % (i, j, i * j), end="")
        j += 1
    i+=1
    print()

# Mit for und einem Tupel
num = (list(range(1,11)))
for i in num:
    for j in num:
        print('%3dx%3d=%3d\t' % (i, j, i * j), end="")
    print()
print(120 * "#")


