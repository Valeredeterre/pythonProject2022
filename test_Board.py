import unittest
from board import Board
from piece import *

chessboard = Board()
chessboard1 = Board()



def chessboard_clear():
    for x in range(8):
        for y in range(8):
            chessboard.board[x][y] = Vide(0, 0)


def test_piece_setup(piece: str):
    match piece:
        case 'P':
            chessboard.board[3][3] = Pion('B', 0, 0)
        case 'T':
            chessboard.board[3][3] = Tour('B', 0, 0)
        case 'C':
            chessboard.board[3][3] = Cavalier('B', 0, 0)
        case 'D':
            chessboard.board[3][3] = Dame('B', 0, 0)
        case 'R':
            chessboard.board[3][3] = Roi('B', 0, 0)
        case 'F':
            chessboard.board[3][3] = Fou('B', 0, 0)


class TestBoard(unittest.TestCase):
    chessboard_clear()
    cavalier = 'C'
    fou = 'F'

    def test_boolean_ans_isdeplacementcavalier(self):
        test_piece_setup(self.cavalier)
        self.assertAlmostEqual(chessboard.isdeplacement_cavalier(3, 3, 4, 5), 1)
        self.assertAlmostEqual(chessboard.isdeplacement_cavalier(3, 3, 5, 5), 0)
        chessboard_clear()

    def test_values_isdeplacementcavalier(self):
        test_piece_setup(self.cavalier)
        self.assertRaises(IndexError, chessboard.isdeplacement_cavalier, 3, 3, -1, 2)
        chessboard_clear()

    def test_boolean_ans_isdeplacementfou(self):
        test_piece_setup(self.fou)
        self.assertAlmostEqual(chessboard.isdeplacement_fou(3, 3, 6, 6), 1)
        self.assertAlmostEqual(chessboard.isdeplacement_fou(3, 3, 7, 3), 0)
        chessboard_clear()

    def test_values_isdeplacementfou(self):
        test_piece_setup(self.fou)
        self.assertRaises(IndexError, chessboard.isdeplacement_fou, 3, 3, 8, 8)
        chessboard_clear()



test = TestBoard()
test.test_boolean_ans_isdeplacementcavalier()
test.test_values_isdeplacementcavalier()
test.test_values_isdeplacementfou()
test.test_boolean_ans_isdeplacementfou()



