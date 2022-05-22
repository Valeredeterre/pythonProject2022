import unittest
from board import Board


class TestIsDeplacementCavalier(unittest.TestCase):
    def test_boolans(self):
        self.assertAlmostEqual(Board.isdeplacement_cavalier(Board, 0, 0, 1, 2), 1)
        self.assertAlmostEqual(Board.isdeplacement_cavalier(Board, 0, 0, 0, 2), 0)

    def test_values(self):
        self.assertRaises(IndexError, Board.isdeplacement_cavalier, Board, 0, 0, -1, 2)

test = TestIsDeplacementCavalier()
test.test_boolans()
test.test_values()



