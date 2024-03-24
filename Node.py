# The tree is going to be a tree of all the moves in the game.
# The root will always be the current board state.
# Every time a move is made, the new root will be the new board state.

# The node stores the move and the index of the optimal move to make from that state.
class Node:
    def __init__(self, move):
        self.move = move
        self.gameValue = None
        self.bestMoveIndex = None
        self.childs = []
