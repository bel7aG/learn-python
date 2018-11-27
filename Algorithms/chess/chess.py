mainBoard=[
[0,0,0,0,0,0,0,0],
[9,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
]
mainBoard=[[0 for i in range(8)] for j in range(8)]

def test(mainBoard,lig,col):
    for i in range(8):
        if(mainBoard[i][col]==9):
            return False
    for i in range(8):
        if(mainBoard[lig][i]==9):
            return False
    for j in range(8):
        for k in range(8):
            if(mainBoard[j][k]==9):
                if(abs(j-lig)==abs(k-col)):
                    return False
    return True
def queen(mainBoard,col):
    v = 0
    if(col==8):
        return True
    for i in range(8):
        if(test(mainBoard,i,col)==True):
            v += 1
            mainBoard[i][col]=9
            if(queen(mainBoard,col+1)==True):
                return True
            else:
                mainBoard[i][col]=0

queen(mainBoard,0)
for i in range(8):
    print(mainBoard[i])
