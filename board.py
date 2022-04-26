class Board:
    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        board = [[str(".") for i in range(8)] for j in range(8)]
        return board

    def __repr__(self):
        str = ""
        for k in range(8):
            str += "\n"
            for j in range(8):
                str += self.board[j][k]
        return str

    def get(self, x, y):
        return self.board[x][y]

    def set(self, x, y, value):
        self.board[x][y] = value


class Piece:
    def __init__(self, type, x, y, board):
        self.type = type
        board.set(x,y,self.type)

    def deplacement(self, dx, dy, ax, ay, board):
       if(board.board[dx][dy] != "."):
            if(board.board[ax][ay] == "."):
                board.set(dx, dy, ".")
                board.set(ax,ay,self.type)
            else: print("deja une piece")
       else: print("pas de piece à cet emplacement")



board1 = Board()

K1 = Piece("K",2,0,board1)

print(board1)

K1.deplacement(2,0,0,1,board1)

print(board1)