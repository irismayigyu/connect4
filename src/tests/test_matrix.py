import unittest
from services.matrix import Matrix


class TestMatrix(unittest.TestCase):
    '''Testiluokka matrixille ja sovelluslogiikalle'''

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

    def test_if__winning_checker_works_diag_up(self):
        self.matrix.player = "X"
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, "X"],
                            [0, 0, 0, 0, 0, "X", 0],
                            [0, 0, 0, 0, "X", 0, 0],
                            [0, 0, 0, "X", 0, 0, 0]]
        self.assertEqual(self.matrix.checker("X"), True)

    def test_if__winning_checker_works_diag_down(self):
        self.matrix.player = "X"
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, "X", 0, 0, "O"],
                            [0, 0, 0, 0, "X", 0, "O"],
                            [0, 0, 0, 0, 0, "X", 0],
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

    def test_full_checker(self):
        self.matrix.grid = [["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"]]
        self.assertEqual(self.matrix.full(), True)

    def test_full_checker_false(self):
        self.matrix.grid = [["X", "X", "X", 0, "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"]]
        self.assertEqual(self.matrix.full(), False)

    def test_make_move(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, "X", "X"]]
        self.matrix.make_move(5, "O")
        self.assertEqual(self.matrix.grid, [[0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, "O", 0],
                                            [0, 0, 0, 0, 0, "X", "X"]])

    def test_make_move_false(self):
        self.matrix.grid = [["X", "X", "X", 0, "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"],
                            ["X", "X", "X", "X", "X", "X", "X"]]
        self.matrix.make_move(5, "O")
        self.assertEqual(self.matrix.grid, [["X", "X", "X", 0, "X", "X", "X"],
                                            ["X", "X", "X", "X", "X", "X", "X"],
                                            ["X", "X", "X", "X", "X", "X", "X"],
                                            ["X", "X", "X", "X", "X", "X", "X"],
                                            ["X", "X", "X", "X", "X", "X", "X"],
                                            ["X", "X", "X", "X", "X", "X", "X"]])
        self.assertEqual(self.matrix.make_move(5, "O"), False)

    def test_change_players(self):
        self.matrix.player = "O"
        self.matrix.change_turns()
        self.assertEqual(self.matrix.player, "X")
