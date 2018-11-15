from random import randint
from random import sample
t = [i for i in range(10)]

ranX = sample(t, 4)
for i in range(len(ranX)):
    ranX[i] = str(ranX[i])

lol = ''.join(ranX)


def isFoor(data):
    if (len(data) == 4):
        for myChar in data:
            x = data.count(myChar)
            if (ord(myChar) < ord("0") and ord(myChar) > ord("9")):
                print("must be digits not characters")
                return False
            if x > 1:
                print("you have repeated digit.")
                return False
    else:
        print("must be 4 digits.")
    return data


hardwareChoiceString = lol


print(hardwareChoiceString)

notYet = True
while (notYet):
    x = (input("put a number with 4 degits: "))
    countCow = 0
    countToro = 0
    for i in range(4):
        for j in range(4):
            if (hardwareChoiceString[i] == x[j]):
                if (i == j):
                    countToro = countToro + 1
                else:
                    countCow = countCow + 1


    print("\n\n\n\tCow: ", countCow, "\n")
    print("\n\tToto: ", countToro, "\n")
    if countToro == 4:
        notYet = False
        print("Congratlation you guessed it and it is ", hardwareChoiceString)
        exit()
    countCow = countToro = 0
