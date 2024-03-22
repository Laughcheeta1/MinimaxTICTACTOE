class Board:
    # The rules stay the same even for boards bigger than 3, you have to make 3 in a row

    def __init__(self, boardSize):
        self.turnNumber = 0
        self.moves = []
        # The board will be a 2D array, can be whatever board size you want
        self.boardSize = (boardSize[0] if boardSize[0] > 3 else 3, boardSize[1] if boardSize[1] > 3 else 3)
        self.requiredWin = min(self.boardSize[0], self.boardSize[1]) # Create the required connections to win depending on the grid
        print(f"The win Is {self.requiredWin}")
        # Initialize the board
        self.board = [ [ " " for _ in range(self.boardSize[1]) ] for _ in range(self.boardSize[0]) ]


    def printBoard(self):
        print(f"\nThe board in the turn {self.turnNumber} looks like this")
        print("    ", end = "")
        for i in range(self.boardSize[1]):
            print(i, end="    ")
        print()
        
        j = 0
        for row in self.board:
            print(j, end=" ")
            print(row)
            j += 1


    # Return values:
    # "I" -> Invalid move
    # "A" -> Accepted move
    # "T" -> Tie
    # winner -> Finished game (The move produced a winner)
    def enterMove(self, move):
        if (move[0] < 0 or move[0] >= self.boardSize[0]) or (move[1] < 0 or move[1] >= self.boardSize[1]):
            return "I"
        if self.board[move[0]][move[1]] != " ":
            return "I"

        # Both this if statements could be done in a single If, but for readability, I prefer to 
        # divide them.
        
        if self.turnNumber % 2 == 0:
            self.board[move[0]][move[1]] = "X"
        else:
            self.board[move[0]][move[1]] = "O"
        
        self.turnNumber += 1
        self.moves.append(move)

        if self.checkFinalState():
            return "X" if (self.turnNumber - 1) % 2 == 0 else "O"

        if self.turnNumber == self.boardSize[0] * self.boardSize[1]:
            return "T"

        return "A"
    
    def checkFinalState(self):
        # Instead of constantly checking the whole board is better to just check the last
        # move made, and see if it generated a win condition (3 in a row).
        lastMove = self.moves[-1]
        value = self.board[lastMove[0]][lastMove[1]]

        return (
            self.checkRow(value, lastMove) or
            self.checkColumn(value, lastMove) or
            self.checkDiagonals(value, lastMove)
        )
    
    def checkRow(self, value, move):
        # check left side
        i = 0
        while i < self.requiredWin and move[1] - i >= 0 and self.board[move[0]][move[1] - i] == value:
            i += 1
        
        if i == self.requiredWin:
            return True
        
        # check right side
        i = 0
        while i < self.requiredWin and move[1] + i < self.boardSize[1] and self.board[move[0]][move[1] + i] == value:
            i += 1
        
        return True if i == self.requiredWin else False
    

    def checkColumn(self, value, move):
        # check top
        i = 0
        while i < self.requiredWin and move[0] - i >= 0 and self.board[move[0] - i][move[1]] == value:
            i += 1
        
        if i == self.requiredWin:
            return True
        
        # check bottom
        i = 0
        while i < self.requiredWin and move[0] + i < self.boardSize[0] and self.board[move[0] + 1][move[1]] == value:
            i += 1
        
        return True if i == self.requiredWin else False

    def checkDiagonals(self, value, move):
        # check top left
        i = 0
        while i < self.requiredWin and move[0] - i >= 0 and move[1] - i >= 0 and self.board[move[0] - i][move[1] - i] == value:
            i += 1
        
        if i == self.requiredWin:
            return True
        
        # check bottom right
        i = 0
        while i < self.requiredWin and move[0] + i < self.boardSize[0] and move[1] + i < self.boardSize[1] and self.board[move[0] + i][move[1] + i] == value:
            i += 1
        
        if i == self.requiredWin:
            return True
        
        # check top right
        i = 0
        while i < self.requiredWin and move[0] - i >= 0 and move[1] + i < self.boardSize[1] and self.board[move[0] - i][move[1] + i] == value:
            i += 1
        
        if i == self.requiredWin:
            return True
        
        # check bottom left
        i = 0
        while i < self.requiredWin and move[0] + i < self.boardSize[0] and move[1] - i >= 0 and self.board[move[0] + i][move[1] - i] == value:
            i += 1
        
        return True if i == self.requiredWin else False