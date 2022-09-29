s = '/home/myName/images/image1.jpg'
lastPos = s.rfind('/')
filename = s[lastPos+1:]
path = s[:lastPos-1]
print(filename)
print(path)

#oder kürzer
print("Dateiname: " + s[s.rfind('/')+1:] + "\nPfad: " + s[:s.rfind('/')-1])