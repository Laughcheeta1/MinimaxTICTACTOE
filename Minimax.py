from Board import Board

def getAvailableMoves(board):
    """
    Returns a list of available moves for the given board.
    """
    availableMoves = []
    for i in range(board.boardSize[0]):
        for j in range(board.boardSize[1]):
            if board.board[i][j] == " ":
                availableMoves.append((i, j))
    
    return availableMoves


def minimax(board, player):
    pass