class Board:
    def __init__(self):
        self.turnNumber = 0
        
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]


    def printBoard(self):
        print(f"\nThe board in the turn {self.turnNumber} looks like this")
        print("    ", end = "")
        for i in range(3):
            print(i, end="    ")
        print()
        
        j = 0
        for row in self.board:
            print(j, end=" ")
            print(row)
            j += 1


    def enterMove(self, move):
        if self.board[move[0]][move[1]] != " ":
            return False
        
        if self.turnNumber % 2 == 0:
            self.board[move[0]][move[1]] = "X"
        else:
            self.board[move[0]][move[1]] = "O"
        
        self.turnNumber += 1
        return True