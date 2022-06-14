from piece import *
from board import Board
import pygame
import math


def deplacement_piece(chess, turn, colour, select=None):
    chess.board_display(screen, colour)
    pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_end = pygame.mouse.get_pos()
        local_new_x = math.floor(mouse_end[0] / 50)
        local_new_y = math.floor(mouse_end[1] / 50)
        if select is not None:

            if chess.isdeplacement(select[0],select[1],local_new_x, local_new_y) and chess.board[select[0]][select[1]].colour == colour:
                chess.deplacement(select[0],select[1],local_new_x, local_new_y)
                select = None
                if turn == "Black":
                    turn = "White"
                elif turn == "White":
                    turn = "Black"
            else:
                return None, turn
        else:
            if chess.board[local_new_x][local_new_y].type != "X" and chess.board[local_new_x][local_new_y].colour == colour:
                select = (local_new_x, local_new_y)
    return select, turn


chess = Board()
chess_turn_start = Board()
pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((400, 400))
screen.blit(pygame.image.load("ImagesPieces/start_screen.png"), (0, 0))
pygame.display.flip()
running = True
select = None
turn = "White"
n = 1
game_over = False

while running:
    for event in pygame.event.get():

        print(turn, n)
        print(select)
        n += 1


        if game_over is not True:
            chess_turn_start.board = chess.board

            if turn == "White":
                (select, turn) = deplacement_piece(chess, turn, 'W', select)

            elif turn == "Black":
                (select, turn) = deplacement_piece(chess, turn, 'B', select)

            pygame.display.flip()

            if chess.ischeck("W"):
                chess.board = chess_turn_start.board
                print("les blancs sont echec")
                turn = "White"
                pygame.display.flip()

            if chess.ischeck("B"):
                chess.board = chess_turn_start.board
                print("les noirs sont echec")
                turn = "Black"
                pygame.display.flip()

            if select is not None:
                screen.blit(pygame.image.load("ImagesPieces/select.png"), (50 * select[0], 50 * select[1]))
                pygame.display.flip()


        if event.type == pygame.QUIT:
            running = False