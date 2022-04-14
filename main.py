
class Board:
    def __init__(self):
        self.board = self.initialize()

    def initialize(self):
        board = [["X" for i in range(8)] for j in range(8)]
