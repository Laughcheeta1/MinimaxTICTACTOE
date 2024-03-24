from Board import Board
from Node import Node
import random

class Minimax:
    # X will be the maximizing player (1)
    # O will be the minimizing player (-1)
    # The tie condition will be 0
    def __init__(self, board, isMaximixingPlayer):
        self.game = board
        self.isMaximixingPlayer = isMaximixingPlayer
        self.gameTree = Node(None)
        self.calculateValue(self.gameTree, isMaximixingPlayer)
        print("Just checking everything is working fine")


    # This gets the value of the 
    def calculateValue(self, currentNode, isMaximixingPlayer):
        res = self.game.checkCurrentState()
        if res == "X": # X winning
            currentNode.gameValue = 1
            return
        if res == "O": # O winning
            currentNode.gameValue = -1
            return
        if res == "T": # Tie
            currentNode.gameValue = 0
            return
        
        currentNode.childs = [Node(move) for move in self.game.getAvailableMoves()]

        # Pass get the value of each of the child nodes
        for childNode in currentNode.childs:
            self.game.enterMove(childNode.move)
            self.calculateValue(childNode, not isMaximixingPlayer)
            self.game.revertMove()
        
        # Fill the best move and the value of the current node
        if isMaximixingPlayer:
            currentNode.gameValue, currentNode.bestMove = self.findMaxValue(currentNode)
        else:
            currentNode.gameValue, currentNode.bestMove = self.findMinValue(currentNode)
        # currentNode.gameValue, currentNode.bestMove = self.findMaxValue(currentNode) if isMaximixingPlayer else self.findMinValue(currentNode)
        

    # As there can be a lot of max (or min) moves that can give maximum or minimum, just pick one random, as to not make all games feel equal
    # (Even tho they are)
    def findMinValue(self, node):
        currentMin = float("inf")
        minMoves = []
        for childNode in node.childs:
            if childNode.gameValue < currentMin: # If there is a new min, clear the list of moves and start with the min
                currentMin = childNode.gameValue
                minMoves = []
            if childNode.gameValue == currentMin:
                minMoves.append(childNode.move)

        return currentMin, random.choice(minMoves)


    # As there can be a lot of max (or min) moves that can give maximum or minimum, just pick one random, as to not make all games feel equal
    # (Even tho they are)
    def findMaxValue(self, node):
        currentMax = float("-inf") # Maximum value we have found
        maxMoves = [] # Moves that will get us the maximum value
        for childNode in node.childs:
            if childNode.gameValue > currentMax: # If there is a new max, clear the list of moves and start with the min
                currentMax = childNode.gameValue
                maxMoves = []
            
            if childNode.gameValue == currentMax:
                maxMoves.append(childNode.move)

        return currentMax, random.choice(maxMoves)