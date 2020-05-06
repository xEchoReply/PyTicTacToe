def winningBoard(gameBoard,i):
    if (
    #Check rows
    gameBoard[0][0:3]==[i,i,i] or
    gameBoard[1][0:3]==[i,i,i] or
    gameBoard[2][0:3]==[i,i,i] or
    #Check columns
    (gameBoard[0][0]==i and gameBoard[1][0]==i and gameBoard[2][0]==i) or
    (gameBoard[0][1]==i and gameBoard[1][1]==i and gameBoard[2][1]==i) or
    (gameBoard[0][2]==i and gameBoard[1][2]==i and gameBoard[2][2]==i) or
    #Check diagnals
    (gameBoard[0][0]==i and gameBoard[1][1]==i and gameBoard[2][2]==i) or
    (gameBoard[0][2]==i and gameBoard[1][1]==i and gameBoard[2][0]==i)
    ):
        return i

def checkWinner(gameBoard):
    if (winningBoard(gameBoard,1)==1):
        return 1
    elif (winningBoard(gameBoard,2)==2):
        return 2
    else:
        return 0

def drawBoard(myGame):
    myGameBoard="   7   8   9 \n  --- --- ---\n7| "+str(myGame[0][0])+" | "+str(myGame[0][1])+" | "+str(myGame[0][2])+" |\n  --- --- ---\n8| "+str(myGame[1][0])+" | "+str(myGame[1][1])+" | "+str(myGame[1][2])+" |\n  --- --- ---\n9| "+str(myGame[2][0])+" | "+str(myGame[2][1])+" | "+str(myGame[2][2])+" |\n  --- --- ---"
    myGameBoard=myGameBoard.replace("0", " ")
    myGameBoard=myGameBoard.replace("1", "X")
    myGameBoard=myGameBoard.replace("2", "O")
    myGameBoard=myGameBoard.replace("7", "1")
    myGameBoard=myGameBoard.replace("8", "2")
    myGameBoard=myGameBoard.replace("9", "3")
    print(myGameBoard)

def playerTurn(turn):
        testValid=0
        while testValid!=1:
            choice=input("Player "+str(turn)+" choose a square (row,col): ")
            try:
                if myGame[(int(choice[0])-1)][(int(choice[2])-1)]!=0:
                    print("This spot is taken!")
                else:
                    testValid=1
                    myGame[(int(choice[0])-1)][(int(choice[2])-1)]=turn
            except:
                print("Incorrect format!")

myGame=[[0,0,0],
        [0,0,0],
        [0,0,0]]
winner=0
turn=1
draw=""

while winner==0:

    drawBoard(myGame)
    playerTurn(turn)
    winner=checkWinner(myGame)
    if turn==1:
        turn=2
    else:
        turn=1

    if ((not 0 in myGame[0]) and (not 0 in myGame[1]) and (not 0 in myGame[2])):
        draw="Draw!"
        break

drawBoard(myGame)
if draw!="Draw!":
    print("Player "+str(winner)+" wins!")
else:
    print(draw)
