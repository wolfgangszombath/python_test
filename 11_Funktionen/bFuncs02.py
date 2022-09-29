from random import randint


def pwGenerator(n):
    letters = 'abcdefghijklmnopqrstuvwxyz01234546789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max = len(letters)
    lst = [letters[randint(0,max-1)] for _ in range(n)]
    return ''.join(lst)


repeat = 'n'
while repeat == 'n':
    lenPwd = int(input("Wie lange soll ihr Passwort sein?\n"))
    print("Ihr Passwort lautet: \t" , pwGenerator(lenPwd))
    repeat = input("Sind Sie damit zufrieden? (y/n)")
    repeat.lower()
