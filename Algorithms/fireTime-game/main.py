import random

userInput = int(input("your Square Matrix numbers: "))

hellBoard = [[0 for i in range(userInput)] for j in range(userInput)]


def stream(hellBoard):
    print()
    print()
    print()
    for i in range(len(hellBoard)):
        for j in range(len(hellBoard)):
            hellBoard[i][j] = "_*_"
            print("|", hellBoard[i][j], "|", end="   ")
            if (random.randint(0, userInput) == i and random.randint(0, userInput) == j):
                hellBoard[i][j] = "_H_"
                print("|", hellBoard[i][j], "|", end="   ")
            else:
                hellBoard[i][j] = "_*_"


        print()
        print()
        print()
        print()

stream(hellBoard)
