myNumbersList = [0,1,1,2,3,5,8,11,19,30,49,79,78,77]
guessNumber = int(input("Geben Sie eine Zahl zwischen 0 und 79 ein\n"))
trueAnswer = "Die Liste enhält die Zahl " + str(guessNumber) + '!'
falseAnswer = "Die Liste enhält die Zahl " + str(guessNumber) + ' nicht!'
print(trueAnswer if guessNumber in  myNumbersList else falseAnswer)