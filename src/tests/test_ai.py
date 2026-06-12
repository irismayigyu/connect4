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
