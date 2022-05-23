from piece import Piece
from piece import Pion
from player import Player
from board import Board

<<<<<<< HEAD
piece1 = Pion("B", 0, 0)
board1 = Board()
player1 = Player("Val")
print(piece1)
print(player1)
=======
class Board:
    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        board = [["X" for i in range(8)] for j in range(8)]
        return board

    def __repr__(self):
        str = ""
        for k in range(8):
            self.board.append("\n")
            for j in range (8):
                str += self.board[j][k]
        return str

board1 = Board()
print(board1)
>>>>>>> 24b0a64 (Initialisation Board)
