from Board import Board
from Node import Node
import random

# TODO: it is not playin optimally

class Minimax:
    # X will be the maximizing player (1)
    # O will be the minimizing player (-1)
    # The tie condition will be 0
    def __init__(self, board):
        self.game = board
        self.gameTree = Node(None)
        self.possibleGamesFound = 0
        print("Computer is thinking ...")
        self.calculateValue(self.gameTree, True) # Calculate the expected value of the whole game (If playing optimally)
        print(f"Possible games found: {self.possibleGamesFound}")


    def printExpectedOutcome(self):
        print(f"Expected outcome is {'X win' if self.gameTree.gameValue == 1 else 'O win' if self.gameTree.gameValue == -1 else 'Tie'}\n")


    def makeMove(self):
        self.gameTree = self.gameTree.childs[self.gameTree.bestMoveIndex] # Change the tree to the best move
        return self.gameTree.move # Since we changed the tree to the best move, we can return the move


    def registerMove(self, move): # Register the move that the player made
        for child in self.gameTree.childs:
            if child.move == move:
                self.gameTree = child
                return


    # This gets the value of the node. 
    def calculateValue(self, currentNode, isMaximixingPlayer):
        res = self.game.checkCurrentState()
        if res == "X": # X winning
            currentNode.gameValue = 1
            self.possibleGamesFound += 1
            return
        if res == "O": # O winning
            currentNode.gameValue = -1
            self.possibleGamesFound += 1
            return
        if res == "T": # Tie
            currentNode.gameValue = 0
            self.possibleGamesFound += 1
            return
        
        currentNode.childs = [Node(move) for move in self.game.getAvailableMoves()]

        # Pass get the value of each of the child nodes
        for childNode in currentNode.childs:
            self.game.enterMove(childNode.move)
            self.calculateValue(childNode, not isMaximixingPlayer)
            self.game.revertMove()
        
        # Fill the best move and the value of the current node
        if isMaximixingPlayer:
            currentNode.gameValue, currentNode.bestMoveIndex = self.findMaxValue(currentNode)
        else:
            currentNode.gameValue, currentNode.bestMoveIndex = self.findMinValue(currentNode)
        

    # As there can be a lot of max (or min) moves that can give maximum or minimum, just pick one random, as to not make all games feel equal
    # (Even tho the results are)
    def findMinValue(self, node):
        currentMin = float("inf")
        minMoves = []
        minMovesIndexes = []
        i = 0

        for childNode in node.childs:
            if childNode.gameValue < currentMin: # If there is a new min, clear the list of moves and start with the min
                currentMin = childNode.gameValue
                minMoves = []
                minMovesIndexes = []

            if childNode.gameValue == currentMin:
                minMoves.append(childNode.move)
                minMovesIndexes.append(i)

            i += 1

        return currentMin, random.choice(minMovesIndexes) # Get a random index in the list of best moves


    # As there can be a lot of max (or min) moves that can give maximum or minimum, just pick one random, as to not make all games feel equal
    # (Even tho they are)
    def findMaxValue(self, node):
        currentMax = float("-inf") # Maximum value we have found
        maxMoves = [] # Moves that will get us the maximum value
        maxMovesIndexes = []
        i = 0

        for childNode in node.childs:
            if childNode.gameValue > currentMax: # If there is a new max, clear the list of moves and start with the min
                currentMax = childNode.gameValue
                maxMoves = []
                maxMovesIndexes = []
            
            if childNode.gameValue == currentMax:
                maxMoves.append(childNode.move)
                maxMovesIndexes.append(i)
            
            i += 1

        return currentMax, random.choice(maxMovesIndexes) # Get a random index in the list of best moves