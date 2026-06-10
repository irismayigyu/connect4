import unittest
from src.services.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_if__winning_checker_works_row(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, "X", "X", "X", "X"]]
        self.matrix.player = "X"
        self.assertEqual(self.matrix.checker("X"), True)

    def test_if__winning_checker_works_column(self):
        self.matrix.player = "X"
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, "X"],
                            [0, 0, 0, 0, 0, 0, "X"],
                            [0, 0, 0, 0, 0, 0, "X"],
                            [0, 0, 0, 0, 0, 0, "X"]]
        self.assertEqual(self.matrix.checker("X"), True)

    def test_if_correct_player_wins(self):
        self.matrix.player = "O"
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, "X", "X", "X", "X"]]
        self.assertEqual(self.matrix.checker("O"), False)
