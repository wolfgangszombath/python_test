a=['a','d','g']
b=['a']
msg = str(a)+" gleich "+str(b) if a == b else str(a)+" nicht gleich "+str(b)
print (msg)
b.append('d')
msg = str(a)+" gleich "+str(b) if a == b else str(a)+" nicht gleich "+str(b)
print (msg)
b.append('g')
msg = str(a)+" gleich "+str(b) if a == b else str(a)+" nicht gleich "+str(b)
print (msg)
msg = "Die Objekte sind gleich " if a is b else "Die Objekte sind nicht gleich"
print (msg)
a = b
msg = "Die Objekte sind gleich " if a is b else "Die Objekte sind nicht gleich"
print (msg)