class Board:
    # The rules stay the same even for boards bigger than 3, you have to make 3 in a row

    def __init__(self, boardSize):
        self.turnNumber = 0
        self.moves = []
        # The board will be a 2D array, can be whatever board size you want
        self.boardSize = (boardSize[0] if boardSize[0] > 3 else 3, boardSize[1] if boardSize[1] > 3 else 3)
        self.requiredWin = min(self.boardSize[0], self.boardSize[1]) # Create the required connections to win depending on the grid
        # Initialize the board
        self.board = [ [ " " for _ in range(self.boardSize[1]) ] for _ in range(self.boardSize[0]) ]


    # Returns the player who is to play
    def turn(self):
        return "X" if self.turnNumber % 2 == 0 else "O"


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
    # "C" -> Game continues
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

        return self.checkCurrentState()


    def revertMove(self):
        if self.turnNumber == 0:
            return
        
        move = self.moves.pop()
        self.board[move[0]][move[1]] = " "
        self.turnNumber -= 1


    # "C" -> Game continues
    # "T" -> Tie
    # winner -> Finished game (The move produced a winner)
    def checkCurrentState(self):
        if self.turnNumber == 0:
            return "C"

        if self.checkFinalState():
            return "X" if (self.turnNumber - 1) % 2 == 0 else "O"
        
        if self.turnNumber == self.boardSize[0] * self.boardSize[1]:
            return "T"
        
        return "C"
    

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
        # Go to the left side
        i = move[1]
        while i > 0:
            if self.board[move[0]][i - 1] != value:
                break
            i -= 1
        
        if i == self.requiredWin:
            return True
        
        # check right side
        counter = 0
        while counter < self.requiredWin and i < self.boardSize[1] and self.board[move[0]][i] == value:
            i += 1
            counter += 1
        
        return True if counter == self.requiredWin else False
    

    def checkColumn(self, value, move):
        # Go to the top
        j = move[0]
        while j > 0:
            if self.board[j - 1][move[1]] != value:
                break
            j -= 1
        
        # check bottom
        counter = 0
        while counter < self.requiredWin and j < self.boardSize[0] and self.board[j][move[1]] == value:
            j += 1
            counter += 1
        
        return True if counter == self.requiredWin else False


    def checkDiagonals(self, value, move):
        # Remember j is the row and i is the column
        # Move to the top left corner of the diagonal (or presumed diagonal)
        j = move[0]
        i = move[1]
        while i > 0 and j > 0: # If it is already in a corner, we dont want to go further than that
            if self.board[j - 1][i - 1] != value:
                break
            i -= 1
            j -= 1
    
        # Check the diagonal in a down-right direction
        counter = 0
        while i < self.boardSize[1] and j < self.boardSize[0] and self.board[j][i] == value and counter < self.requiredWin:
            # The last condition is unnecesary but it is intended to avoid checking more than necessary (example: a 3 x 1000 board)
            i += 1
            j += 1
            counter += 1

        if counter == self.requiredWin:
            return True

        # Move to the bottom left corner of the diagonal (or presumed diagonal)
        j = move[0]
        i = move[1]
        while j < self.boardSize[0] - 1 and i > 0:
            if self.board[j + 1][i - 1] != value:
                break
            i -= 1
            j += 1

        counter = 0
        while i < self.boardSize[1] and j >= 0 and self.board[j][i] == value and counter < self.requiredWin:
            # The last condition is unnecesary but it is intended to avoid checking more than necessary (example: a 3 x 1000 board)
            i += 1
            j -= 1
            counter += 1

        return True if counter == self.requiredWin else False


    def getAvailableMoves(self):
        """
        Returns a list of available moves for the given board.
        """
        availableMoves = []
        for i in range(self.boardSize[0]):
            for j in range(self.boardSize[1]):
                if self.board[i][j] == " ":
                    availableMoves.append((i, j))
        
        return availableMoves