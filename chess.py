from board import Board


class Player:
    def __init__(self, name):
        self.name = name
        self.win_nb = 0


class Chess:
    def __init__(self):
        self.player1 = Player("Player1")
        self.player1 = Player("Player2")

    def ischeckmate(self):
        for k in range(8):
            for j in range(8):
                if self.board[j][k].type == "R" and self.board[j][k].colour == "B":




    def game(self):
        while()