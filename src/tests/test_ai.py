import unittest
from services.matrix import Matrix
from ai import AI


class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()
        self.matrix = Matrix()

    def test_possible_moves(self):
        self.matrix.grid = [[0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "X", 0, 0, 0, "X"],
                            ["O", 0, "X", 0, 0, 0, "X"],
                            ["O", 0, "O", 0, 0, 0, "X"],
                            ["O", 0, "O", "X", 0, 0, "X"]]
        self.assertEqual(self.ai.possible_moves(
            self.matrix), [3, 4, 1, 5, 0])

    def test_three_in_a_row(self):
        self.matrix.grid = [[0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "X", 0, 0, 0, "O"],
                            ["O", 0, "X", 0, 0, 0, "X"],
                            ["O", 0, "O", 0, 0, 0, "X"],
                            ["O", "O", "O", "X", 0, 0, "X"]]
        self.assertEqual(self.ai.three_in_a_row(
            self.matrix, "O"), 3)

    def test_evaluate(self):

        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, "O", 0, 0],
                            ["O", "X", "O", "O", 0, "O", 0],
                            ["X", 0, "X", "O", 0, 0, "O"]]
        self.assertEqual(self.ai.evaluate(
            self.matrix, 3), 10)

        self.matrix.grid = [[0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "X", 0, 0, 0, "O"],
                            ["O", 0, "X", 0, 0, 0, "X"],
                            ["O", 0, "O", 0, 0, 0, "X"],
                            ["O", "O", "O", "O", 0, 0, "X"]]
        self.assertEqual(self.ai.evaluate(
            self.matrix, 1), 1001)

        self.matrix.grid = [[0, 0, "O", 0, 0, 0, 0],
                            [0, 0, "O", 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", 0, "O", "X", 0, 0, 0],
                            ["X", "X", "X", "X", 0, 0, 0]]
        self.assertEqual(self.ai.evaluate(
            self.matrix, 1), -1001)

        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", "X", "O", "X", 0, 0, 0],
                            ["X", "X", "X", 0, "X", 0, 0]]
        self.assertEqual(self.ai.evaluate(
            self.matrix, 1), -500)

    def test_game_ended(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", 0, "O", 0, 0, 0, 0],
                            ["X", "X", "X", "X", 0, 0, 0]]
        self.assertEqual(self.ai.game_ended(self.matrix), True)

    def test_best_move(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", 0, "O", 0, 0, 0, 0],
                            ["o", "X", "X", "X", 0, 0, 0]]
        self.assertEqual(self.ai.best_move(self.matrix), 4)

    def test_best_move_middle_start(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.ai.best_move(self.matrix), 3)
