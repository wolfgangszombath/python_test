dict = {'Tom': 38, 'Mary' :32, 'Lewis': 37, 'Kim': 60}
dict.update({'Wolf' : 41})
print(dict)
resultSet = {x for x in dict}
print(resultSet)
resultList = [itm for itm in dict]
print(resultList)

print({key for key,value in dict.items()})
print(sorted({value for key,value in dict.items()}))

