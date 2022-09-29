r = input("Geben Sie den Wert für die Farbe rot ein (0 - 255)")
ir = int(r)
g = input("Geben Sie den Wert für die Farbe rot ein (0 - 255)")
ig = int(g)
b = input("Geben Sie den Wert für die Farbe rot ein (0 - 255)")
ib = int(b)
print("Die von Ihnen eingebene Farbe im rgb Code ist rgb("+r+","+g+","+b+")")
hexR = hex(ir)
hexG = hex(ig)
hexB = hex(ib)
# Umwandlung in Hexcode
r = hexR.strip('0x')
g = hexG.strip('0x')
b = hexB.strip('0x')

print("#" + r+g+b)
#Umwandlung in CMY
c = (255 - ir)//255 * 100
m = (255 - ig)//255 * 100
y = int((255 - ib)/255 * 100)
strC = str(c)
strM = str(m)
strY = str(y)
print("CMY: "+ strC + ',' + strM + ',' + strY )