from Board import Board
from Minimax import Minimax

class Game:
    def __init__(self):
        self.player = self.getPlayerTurn()
        size = [int(input("Enter the number of rows: ")), int(input("Enter the number of columns: "))]
        self.board = Board(size)

        # Minimax is intended to search for the path to victory from the beginning
        self.computer = Minimax(self.board)
        self.board.printBoard()
        self.computer.printExpectedOutcome()

        while self.nextTurn():
            self.board.printBoard()
            self.computer.printExpectedOutcome()


    # Returns if the game should continue or not
    def nextTurn(self):
        if self.board.turn() == self.player:
            result = self.playerTurn()
        else:
            result = self.computerTurn()

        if result == "C":
            return True

        if result == "T":
            self.board.printBoard()
            print("The game resulted in a Tie!!!")
            return False
        
        self.board.printBoard()
        print(f"{result} won the game!!!")
        return False


    def computerTurn(self):
        return self.board.enterMove(self.computer.makeMove())


    # Returns true if the game continues, else returns false
    def playerTurn(self):
        input_given = input("Enter the next move: ").replace(" ", "").split(",") # Remove all spaces and split by comma
        move = (int(input_given[0]), int(input_given[1]))
        result = self.board.enterMove(move)
        
        while result == "I": # Prompt the user to enter a valid until he cooperates
            print("Enter a valid position")
            input_given = input("Enter the next move: ").split(", ")
            move = (int(input_given[0]), int(input_given[1]))
            result = self.board.enterMove(move)

        self.computer.registerMove(move) # Computer registers the move made by the human
        return result


    # Just ask if the player is to be X or O
    def getPlayerTurn(self):
        humanTurn = input("You want to play as X or O?: ").upper()
        while humanTurn != "X" and humanTurn != "O":
            humanTurn = input("You want to play as X or O?: ")

        return humanTurn