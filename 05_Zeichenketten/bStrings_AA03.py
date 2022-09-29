hexcode = input("Geben Sie den Farbcode einer bestimmten Farbe ein (z.B #111111)\n")
r = hexcode[1:3]
g = hexcode[3:5]
b = hexcode[5:7]
rgbR = int(r,16)
rgbG = int(g,16)
rgbB = int(b,16)
print(hexcode + " umgewandelt in RGB: " + str(rgbR) + ',' + str(rgbG) + ',' + str(rgbB))