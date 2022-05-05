from piece import Piece
from piece import Pion
from piece import Roi
from piece import Dame
from piece import Fou
from piece import Tour
from piece import Cavalier




class Board:
    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        board = [["X" for i in range(8)] for j in range(8)]
        for i in range(8):
            board[i][1] = "P"
            board[i][6] = "P"

        for i in range(0, 8, 7): # i = 0 then i = 0 + 7
            if(i == 0):
                colour = "B"
                board[0][i] = Tour(colour, 0, i)
                board[1][i] = Cavalier(colour, 1, i)
                board[2][i] = Fou(colour, 2, i )
                board[3][i] = Roi(colour,3 , i)
                board[4][i] = Dame(colour ,4 , i)
                board[5][i] = Fou(colour ,5, i)
                board[6][i] = Cavalier(colour ,6,i)
                board[7][i] = Tour(colour , 7, i)
            else:

        return board

    def __repr__(self):
        str = ""
        for k in range(8):
            str += "\n"
            for j in range(8):
                str += self.board[j][k]
        return str

    def get_case_value(self, x, y):
        return self.board[x][y]

    def case_status(self, x ,y): # a return value of 0 refers to an empty case
        if (self.get_case_value(x, y) != "X"):
            return 1
        else:
            return 0


chessboard = Board()
print(chessboard)
case_value = Board.get_case_value(chessboard, 3, 0)
print(case_value)
case_status = Board.case_status(chessboard, 3, 3)
print(case_status)