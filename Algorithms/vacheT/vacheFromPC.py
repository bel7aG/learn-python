def checkIt(x):
    myArray = []
    for i in range(100, (x + 1)):
        ops = str(i)
        if (len(ops) == 3):
            if (ops[0] != ops[1] and ops[0] != ops[2] and ops[1] != ops[0] and ops[1] != ops[2]):
                myArray.append(i)
        if (len(ops) == 4):
            if (ops[0] != ops[1] and ops[0] != ops[2] and ops[0] !=ops[3] and ops[1] != ops[0] and ops[1] != ops[2] and ops[1] !=ops[3] and ops[2] != ops[0] and ops[2] != ops[1] and ops[2] != ops[3]):
                myArray.append(i)
    print((myArray))


    

checkIt(9999)
