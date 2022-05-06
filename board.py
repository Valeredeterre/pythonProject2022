from piece import Piece
from piece import Pion
from piece import Roi
from piece import Dame
from piece import Fou
from piece import Tour
from piece import Cavalier
from piece import Vide


class Board:

    board = [["X" for i in range(8)] for j in range(8)]
    for i in range(8):
        board[i][2] = Vide(i, 2)
        board[i][3] = Vide(i, 3)
        board[i][4] = Vide(i, 4)
        board[i][5] = Vide(i, 5)

    for i in range(8):
        board[i][1] = Pion("B", i, 1)
        board[i][6] = Pion("B", i, 6)
    for i in range(0, 8, 7):  # i = 0 then i = 0 + 7
        if (i == 0):
            colour = "B"
            board[0][i] = Tour(colour, 0, i)
            board[1][i] = Cavalier(colour, 1, i)
            board[2][i] = Fou(colour, 2, i)
            board[3][i] = Roi(colour, 3, i)
            board[4][i] = Dame(colour, 4, i)
            board[5][i] = Fou(colour, 5, i)
            board[6][i] = Cavalier(colour, 6, i)
            board[7][i] = Tour(colour, 7, i)
        else:
            colour = "W"
            board[0][i] = Tour(colour, 0, i)
            board[1][i] = Cavalier(colour, 1, i)
            board[2][i] = Fou(colour, 2, i)
            board[3][i] = Roi(colour, 3, i)
            board[4][i] = Dame(colour, 4, i)
            board[5][i] = Fou(colour, 5, i)
            board[6][i] = Cavalier(colour, 6, i)
            board[7][i] = Tour(colour, 7, i)

    # def __init__(self):
    # self.board = self.initialize()

    def __repr__(self):
        str = ""
        for k in range(8):
            str += "\n"
            for j in range(8):
                    str += self.board[j][k].type
        return str

    def deplacement_cavalier(self, colour, x, y, new_x, new_y):
        if new_x == x + 1 and new_y == y + 2:
            if self.board[new_x][new_y].type == "X":
                self.board[x][y] = Vide(x, y)
                self.board[new_x][new_y] = Cavalier(colour, new_x, new_y)
            elif self.board[x + 1][y + 2].colour == Board.board[x][y].colour:
                return 'La case est prise'


chessboard = Board()
chessboard.deplacement_cavalier("B", 1, 0, 2, 2)
print(chessboard.board[2][2].type)
print(chessboard.board[1][0].type)
print(chessboard)


