from piece import *
from board import Board
import pygame
import math
import time


def deplacement_piece(chess, turn, colour, select=None):
    """Verify if a move is legitimate for a tower
        This method will take two starting and two ending  positional arguments and verify if the move is legitimate.
        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param
        :param
        :return: return the turn and if a case is selected
        :rtype: bool
    """
    chess.board_display(screen, colour)
    pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_end = pygame.mouse.get_pos()
        local_new_x = math.floor(mouse_end[0] / 50)
        local_new_y = math.floor(mouse_end[1] / 50)
        if select is not None:
            if chess.isdeplacement(select[0],select[1],local_new_x, local_new_y) and chess.board[select[0]][select[1]].colour == colour and (select[0] != local_new_x or select[1] != local_new_y):

                piece = chess.board[select[0]][select[1]].type
                chess.deplacement(select[0],select[1],local_new_x, local_new_y)

                with open('logs.txt', 'a') as f:
                    f.write(piece)
                    f.write(", deplacement = ")
                    f.write(str(select[0]))
                    f.write(" ")
                    f.write(str(select[1]))
                    f.write(" ")
                    f.write(str(local_new_x))
                    f.write(" ")
                    f.write(str(local_new_y))
                    f.write("\n")
                    f.write(chess.__repr__())
                    f.write("\n \n \n \n")

                select = None
                if turn == "B":
                    turn = "W"
                elif turn == "W":
                    turn = "B"

            else:
                return None, turn
        else:
            if chess.board[local_new_x][local_new_y].type != "X" and chess.board[local_new_x][local_new_y].colour == colour:
                select = (local_new_x, local_new_y)
    return select, turn


chess = Board()
board_start_turn = Board()
pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((400, 400))
screen.blit(pygame.image.load("ImagesPieces/start_screen.png"), (0, 0))
pygame.display.flip()
running = True
select = None
turn = "W"
frame = 1
game_over = False



with open('logs.txt', 'a') as f:
    f.write("\n\n\n--------------Nouvelle Partie-----------------\n")
    f.write("----------------------------------------------\n\n")



while running:
    for event in pygame.event.get():

        print(turn, frame)
        frame += 1

        if game_over is not True:

            if turn == "W":
                board_start_turn.copy_board(chess)
                (select, turn) = deplacement_piece(chess, turn, 'W', select)
                if chess.ischeck("W"):
                    chess.copy_board(board_start_turn)
                    print("les blancs sont echec")
                    turn = "W"
                    if frame %50 == 0:
                        if chess.ischeck_mate("W",board_start_turn):
                            game_over = True

            elif turn == "B":
                board_start_turn.copy_board(chess)
                (select, turn) = deplacement_piece(chess, turn, 'B', select)
                if chess.ischeck("B"):
                    chess.copy_board(board_start_turn)
                    print("les noirs sont echec")
                    turn = "B"
                    if frame % 50 == 0:
                        if chess.ischeck_mate("B",board_start_turn):
                            game_over = True




            pygame.display.flip()

            if select is not None:
                screen.blit(pygame.image.load("ImagesPieces/select.png"), (50 * select[0], 50 * select[1]))
                pygame.display.flip()

        if event.type == pygame.QUIT:
            running = False