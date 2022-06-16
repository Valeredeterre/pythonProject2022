from board import Board



class Player:
    def __init__(self, name):
        self.name = name
        self.win_nb = 0


class Chess:

    chessboard = Board()

    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.game_over = bool(0)
        self.fin_tour = 0
        self.tour = "W"
        self.check_w = 0
        self.check_b = 0

    def console_chessgame(self):

        while not self.game_over:

            self.game_over = bool(self.chessboard.ischeck_mate('W')) or bool(self.chessboard.ischeck_mate('B'))

            while self.tour == "W":
                self.game_over = bool(self.chessboard.ischeck_mate('W'))
                self.check_w == self.chessboard.ischeck('W')
                print(self.chessboard)
                print(f'Aux {self.tour} de jouer')
                try:
                    x = int(input('Entrez x :'))
                    y = int(input('Entrez y :'))
                    new_x = int(input('Entrez new_x :'))
                    new_y = int(input('Entrez new_y :'))
                except Exception as e:
                    print(e)
                    self.console_chessgame()
                try:
                    if self.chessboard.board[x][y].colour == self.tour:
                        self.fin_tour = self.chessboard.deplacement(x, y, new_x, new_y)
                        if self.fin_tour and self.chessboard.ischeck('W') == 0:
                            self.tour = "B"
                except Exception as e:
                    print(e)
                    self.console_chessgame()

            while self.tour == "B":
                self.game_over = bool(self.chessboard.ischeck_mate('B'))
                self.check_b == self.chessboard.ischeck('B')
                print(self.chessboard)
                print(f'Aux {self.tour} de jouer')
                try:
                    x = int(input('Entrez x :'))
                    y = int(input('Entrez y :'))
                    new_x = int(input('Entrez new_x :'))
                    new_y = int(input('Entrez new_y :'))
                except Exception as e:
                    print(e)
                    self.console_chessgame()
                try:
                    if self.chessboard.board[x][y].colour == self.tour:
                        self.fin_tour = self.chessboard.deplacement(x, y, new_x, new_y)
                        if self.fin_tour and self.chessboard.ischeck('B') == 0:
                            self.tour = "W"
                except Exception as e:
                    print(e)
                    self.console_chessgame()


chess = Chess()
chess.console_chessgame()



