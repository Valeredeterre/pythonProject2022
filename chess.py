from board import Board


class Player:
    def __init__(self, name):
        self.name = name
        self.win_nb = 0


class Chess:


    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.game_over = 0
        self.fin_tour = 0
        self.tour = "W"

    def chessgame(self):
        chessboard = Board()
        while self.game_over != 1:
            print(chessboard)
            if self.tour == "W":
                print(f'Aux {self.tour} de jouer')
                while self.fin_tour == 0:
                    x = int(input('Entrez x :'))
                    y = int(input('Entrez y :'))
                    new_x = int(input('Entrez new_x :'))
                    new_y = int(input('Entrez new_y :'))
                    if chessboard.board[x][y].colour == self.tour:
                        self.fin_tour = chessboard.deplacement_pion(x, y, new_x, new_y)
                        self.fin_tour = chessboard.deplacement_tour(x, y, new_x, new_y)
                        self.fin_tour = chessboard.deplacement_cavalier(x, y, new_x, new_y)
                        self.fin_tour = chessboard.deplacement_dame(x, y, new_x, new_y)
                        self.fin_tour = chessboard.deplacement_roi(x, y, new_x, new_y)
                        self.fin_tour = chessboard.deplacement_fou(x, y, new_x, new_y)
                        print(chessboard)
            self.game_over = 1


    def ischeckmate(self):
        for k in range(8):
            for j in range(8):
                if self.board[j][k].type == "R" and self.board[j][k].colour == "B":
                    return 0

chess = Chess()
chess.chessgame()
