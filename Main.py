from Board import Board

def main():
    humanTurn, computerTurn = getInitialTurns()
    board = Board()
    board.printBoard()
    board.enterMove([0, 0])
    board.printBoard()

    

def getInitialTurns():
    humanTurn = input("You want to play as X or O?: ")
    while humanTurn != "X" and humanTurn != "O":
        humanTurn = input("You want to play as X or O?: ")

    if humanTurn == "X":
        computerTurn = "O"
    else:
        computerTurn = "X"

    return humanTurn, computerTurn

if __name__ == "__main__":
    main()