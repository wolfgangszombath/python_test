'''
Berechnen Sie die Fakultät der Zahlen von 1 bis 20. (Die Fakultät ist
als das Produkt aller Zahlen bis n definiert. Die Fakultät von 6 ist also
1􀀀2􀀀3􀀀4􀀀5􀀀6 = 720.)
'''
f = 1
for i in range(1, 21):
  f = f * i
  print('Die Fakultät von', i, 'beträgt', f)
