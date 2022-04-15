
class Board:
    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        board = [["X" for i in range(8)] for j in range(8)]
        for i in range(8):
            board[i][1] = "P"
            board[i][6] = "P"

        for i in range(0, 8, 7): # i = 0 then i = 0 + 7
            board[0][i] = "T"
            board[1][i] = "C"
            board[2][i] = "F"
            board[3][i] = "R"
            board[4][i] = "D"
            board[5][i] = "F"
            board[6][i] = "C"
            board[7][i] = "T"
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