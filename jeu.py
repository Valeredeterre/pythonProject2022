from piece import Piece
from piece import Pion
from piece import Roi
from piece import Dame
from piece import Fou
from piece import Tour
from piece import Cavalier
from piece import Vide
from board import Board
import pygame
import math
from CheckMate import *

chessboard = Board()
pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((400, 400))

chessboard.ischeck("W")
chessboard.ischeck("B")
chessboard.ischeck_mate("W")
chessboard.ischeck_mate("B")

def deplacement_piece():
    mouse_start = (-1, -1)
    mouse_end = (-1, -1)
    cases = (-1, -1, -1, -1)
    local_x = -1
    local_y = -1
    local_new_x = -1
    local_new_y = -1

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:

            mouse_start = pygame.mouse.get_pos()
            local_x = math.floor(mouse_start[0]/50)
            local_y = math.floor(mouse_start[1]/50)
            print("base = ", local_x, local_y)

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:

            mouse_end = pygame.mouse.get_pos()
            local_new_x = math.floor(mouse_end[0]/50)
            local_new_y = math.floor(mouse_end[1]/50)
            print("fin = ", local_new_x, local_new_y)

    cases = (local_x, local_y, local_new_x, local_new_y)
    return cases


running = True
while running:
    for event in pygame.event.get():

        depl = deplacement_piece()

        if depl[0] != -1:
            x = depl[0]
            y = depl[1]
        if depl[2] != -1:
            new_x = depl[2]
            new_y = depl[3]
            print(x, y, new_x, new_y)
            piece = chessboard.board[x][y].type
            print(piece)

            if piece == "P":
                chessboard.deplacement_pion(x, y, new_x, new_y)

            if piece == "T":
                chessboard.deplacement_tour(x, y, new_x, new_y)

            if piece == "C":
                chessboard.deplacement_cavalier(x, y, new_x, new_y)

            if piece == "F":
                chessboard.deplacement_fou(x, y, new_x, new_y)

            if piece == "R":
                chessboard.deplacement_roi(x, y, new_x, new_y)

            if piece == "D":
                chessboard.deplacement_dame(x, y, new_x, new_y)



        chessboard.board_display(screen)
        if event.type == pygame.QUIT:
            running = False