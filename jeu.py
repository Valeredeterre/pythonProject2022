import pygame
import math
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
        self.game_over = 0
        self.fin_tour = 0
        self.tour = "W"

    def chessgame(self, depl):
        while self.game_over != 1:
            while self.tour == "W":
                print(f'Aux {self.tour} de jouer')
                try:
                    x = depl[0]
                    y = depl[1]
                    new_x = depl[2]
                    new_y = depl[3]
                except Exception as e:
                    print(e)
                    self.chessgame()
                try:
                    if self.chessboard.board[x][y].colour == self.tour:
                        self.fin_tour = self.chessboard.deplacement_pion(x, y, new_x, new_y)
                        if self.fin_tour == 1:
                            self.tour = "B"
                        self.fin_tour = self.chessboard.deplacement_tour(x, y, new_x, new_y)
                        if self.fin_tour == 1:
                            self.tour = "B"
                        self.fin_tour = self.chessboard.deplacement_cavalier(x, y, new_x, new_y)
                        if self.fin_tour == 1:
                            self.tour = "B"
                        self.fin_tour = self.chessboard.deplacement_dame(x, y, new_x, new_y)
                        if self.fin_tour == 1:
                            self.tour = "B"
                        self.fin_tour = self.chessboard.deplacement_roi(x, y, new_x, new_y)
                        if self.fin_tour == 1:
                            self.tour = "B"
                        self.fin_tour = self.chessboard.deplacement_fou(x, y, new_x, new_y)
                        if self.fin_tour == 1:
                            self.tour = "B"
                except Exception as e:
                    print(e)
                    self.chessgame()

            while self.tour == "B":
                print(f'Aux {self.tour} de jouer')
                try:
                    x = depl[0]
                    y = depl[1]
                    new_x = depl[2]
                    new_y = depl[3]
                except Exception as e:
                    print(e)
                    self.chessgame()

                if self.chessboard.board[x][y].colour == self.tour:
                    self.fin_tour = self.chessboard.deplacement_pion(x, y, new_x, new_y)
                    self.fin_tour = self.chessboard.deplacement_tour(x, y, new_x, new_y)
                    self.fin_tour = self.chessboard.deplacement_cavalier(x, y, new_x, new_y)
                    self.fin_tour = self.chessboard.deplacement_dame(x, y, new_x, new_y)
                    self.fin_tour = self.chessboard.deplacement_roi(x, y, new_x, new_y)
                    self.fin_tour = self.chessboard.deplacement_fou(x, y, new_x, new_y)
                    print(self.chessboard)
                    self.tour = "W"

    def ischeckmate(self):
        for k in range(8):
            for j in range(8):
                if self.board[j][k].type == "R" and self.board[j][k].colour == "B":
                    return 0


class Movement:

    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode((400, 400))
    cases = (-1, -1, -1, -1)

    def __int__(self):
        self.event = pygame.event

    def running_pg(self):
        running = True
        while running:
            for self.event in pygame.event.get():

                game.chessgame(deplacement.deplacement_piece()
                               )
                Chess.chessboard.board_display(self.screen)

                if self.event.type == pygame.QUIT:
                    running = False

    def deplacement_piece(self):

        if self.cases[0] == -1 and self.cases[3] == -1:
            if self.cases[0] != -1:
                x = self.cases[0]
                y = self.cases[1]
            else:
                x = -1
                y = -1

            if self.cases[2] != -1:
                new_x = self.cases[2]
                new_y = self.cases[3]
            else:
                new_x = -1
                new_y = -1
        else: self.cases = (-1, -1, -1, -1)

        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.event.button == 1:
                mouse_start = pygame.mouse.get_pos()
                x = math.floor(mouse_start[0]/50)
                y = math.floor(mouse_start[1]/50)
                print("base = ", x, y)

        if self.event.type == pygame.MOUSEBUTTONUP:
            if self.event.button == 1:
                mouse_end = pygame.mouse.get_pos()
                new_x = math.floor(mouse_end[0]/50)
                new_y = math.floor(mouse_end[1]/50)
                print("fin = ", new_x, new_y)

        self.cases = (x, y, new_x, new_y)
        print(self.cases)

        if self.cases[0] != -1:
            x = self.cases[0]
            y = self.cases[1]
        if self.cases[2] != -1:
            new_x = self.cases[2]
            ney_y = self.cases[3]
            print(x, y, new_x, ney_y)

        return self.cases


game = Chess()
deplacement = Movement()
deplacement.running_pg()

