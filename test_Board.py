import unittest
from board import Board


class TestIsDeplacementCavalier(unittest.TestCase):
    def test_boolean_ans(self):
        self.assertAlmostEqual(Board.isdeplacement_cavalier(Board, 0, 0, 1, 2), 1)
        self.assertAlmostEqual(Board.isdeplacement_cavalier(Board, 0, 0, 0, 2), 0)
        self.assertAlmostEqual(Board.isdeplacement_cavalier(Board, 1, 7, 5, 2), 1)


    def test_values(self):
        self.assertRaises(IndexError, Board.isdeplacement_cavalier, Board, 0, 0, -1, 2)

class TestIsDeplacementFou(unittest.TestCase):
    def test_boolean_ans(self):
        self.assertAlmostEqual(Board.isdeplacement_fou(Board, 0, 0, 3, 3), 1)
        self.assertAlmostEqual(Board.isdeplacement_fou(Board, 3, 3, 3, 3), 0)

    def test_values(self):
        self.assertRaises(IndexError, Board.isdeplacement_fou, Board, 0, 0, -1, -1)



test = TestIsDeplacementCavalier()
test.test_boolean_ans()