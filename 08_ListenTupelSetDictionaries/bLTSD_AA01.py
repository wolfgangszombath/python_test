# Die Auswertung eines Tests ergab......
import random
lst = list([])
for i in range(30):
    n = int(random.uniform(1,6))
    lst.append(n)
print(lst)
count_lst = list([])
for j in range(1,6):
    count_lst.append([j, lst.count(j), round((lst.count(j)/len(lst))*100,2)])
#print (count_lst)
for k in count_lst:
    print(k[0], k[1], str(k[2])+'%', sep='\t')











