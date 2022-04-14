
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
            for j in range(8):
                str += self.board[j][k]
        return str

board1 = Board()
print(board1)
