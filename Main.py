from Board import Board

def main():
    humanTurn, computerTurn = getInitialTurns()
    size = [int(input("Enter the number of rows: ")), int(input("Enter the number of columns: "))]
    board = Board(size)
    board.printBoard()
    while nextTurn(board):
        board.printBoard()


# Returns true if the game continues, else returns false
def nextTurn(board):
    input_given = input("Enter the next move: ").replace(" ", "").split(",") # Remove all spaces and split by comma
    move = (int(input_given[0]), int(input_given[1]))
    result = board.enterMove(move)
    while result == "I":
        print("Enter a valid position")
        input_given = input("Enter the next move: ").split(", ")
        move = (int(input_given[0]), int(input_given[1]))
        result = board.enterMove(move)
    
    if result == "C":
        return True

    if result == "T":
        board.printBoard()
        print("The game resulted in a Tie!!!")
        return False
    
    board.printBoard()
    print(f"{result} won the game!!!")
    return False
    
    

def getInitialTurns():
    humanTurn = input("You want to play as X or O?: ").lower()
    while humanTurn != "x" and humanTurn != "o":
        humanTurn = input("You want to play as X or O?: ")

    if humanTurn == "x":
        computerTurn = "o"
    else:
        computerTurn = "x"

    return humanTurn, computerTurn


if __name__ == "__main__":
    main()