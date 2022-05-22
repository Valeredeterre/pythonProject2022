from board import Board
from piece import Pion
from piece import Roi
from piece import Dame
from piece import Fou
from piece import Tour
from piece import Cavalier
from piece import Vide


class Player:
    def __init__(self, name):
        self.name = name
        self.win_nb = 0


class Chess:
    chessboard = Board()
    old_chessboard = Board()

    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.game_over = 0
        self.fin_tour = 0
        self.tour = "W"
        self.check = 0

    def chessgame(self):

        while self.game_over != 1:

            while self.tour == "W":
                self.check_w == self.chessboard.check('W')
                print(self.chessboard)
                print(f'Aux {self.tour} de jouer')
                try:
                    x = int(input('Entrez x :'))
                    y = int(input('Entrez y :'))
                    new_x = int(input('Entrez new_x :'))
                    new_y = int(input('Entrez new_y :'))
                except Exception as e:
                    print(e)
                    self.chessgame()
                try:
                    self.old_chessboard = self.chessboard
                    if self.chessboard.board[x][y].colour == self.tour:
                        self.fin_tour += self.chessboard.deplacement_pion(x, y, new_x, new_y)
                        self.fin_tour += self.chessboard.deplacement_tour(x, y, new_x, new_y)
                        self.fin_tour += self.chessboard.deplacement_cavalier(x, y, new_x, new_y)
                        self.fin_tour += self.chessboard.deplacement_dame(x, y, new_x, new_y)
                        self.fin_tour += self.chessboard.deplacement_roi(x, y, new_x, new_y)
                        self.fin_tour += self.chessboard.deplacement_fou(x, y, new_x, new_y)
                        if self.fin_tour == 1 and self.chessboard.ischeck('W') == 0:
                            self.tour = "B"
                        print(self.chessboard.ischeck('W'))
                        if self.chessboard.ischeck('W') == 1:
                            self.chessboard = self.old_chessboard
                            self.chessgame()

                        print(self.chessboard)
                except Exception as e:
                    print(e)
                    self.chessgame()

            while self.tour == "B":
                print(self.chessboard)
                print(f'Aux {self.tour} de jouer')
                try:
                    x = int(input('Entrez x :'))
                    y = int(input('Entrez y :'))
                    new_x = int(input('Entrez new_x :'))
                    new_y = int(input('Entrez new_y :'))
                except Exception as e:
                    print(e)
                    self.chessgame()

                if self.chessboard.board[x][y].colour == self.tour:
                    self.fin_tour = self.chessboard.deplacement_pion(x, y, new_x, new_y)
                    if self.fin_tour == 1:
                        self.tour = "W"
                    self.fin_tour = self.chessboard.deplacement_tour(x, y, new_x, new_y)
                    if self.fin_tour == 1:
                        self.tour = "W"
                    self.fin_tour = self.chessboard.deplacement_cavalier(x, y, new_x, new_y)
                    if self.fin_tour == 1:
                        self.tour = "W"
                    self.fin_tour = self.chessboard.deplacement_dame(x, y, new_x, new_y)
                    if self.fin_tour == 1:
                        self.tour = "W"
                    self.fin_tour = self.chessboard.deplacement_roi(x, y, new_x, new_y)
                    if self.fin_tour == 1:
                        self.tour = "W"
                    self.fin_tour = self.chessboard.deplacement_fou(x, y, new_x, new_y)
                    if self.fin_tour == 1:
                        self.tour = "W"
                    print(self.chessboard)
                    self.tour = "W"


chess = Chess()
chess.chessboard.board[4][5] = Roi('W',0,0)
chess.chessboard.board[0][0] = Cavalier('W',0,0)
#chess.chessgame()



