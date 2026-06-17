import unittest
from services.matrix import Matrix
from ai import AI


class TestAI(unittest.TestCase):
    '''Testaa AI-luokkaa sekä AI-luokkaa ja Matrix-luokkaa yhdessä'''

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
        self.matrix.initialize_game()
        self.assertEqual(self.ai.best_move(self.matrix), 3)

    def test_make_move_and_best_move_block(self):
        self.matrix.initialize_game()
        self.matrix.make_move(0, "X")
        self.matrix.make_move(0, "X")
        self.matrix.make_move(0, "X")
        move = self.ai.best_move(self.matrix)
        self.assertEqual(move, 0)

    def test_make_move_and_best_move_win(self):
        self.matrix.initialize_game()
        self.matrix.make_move(0, "O")
        self.matrix.make_move(0, "O")
        self.matrix.make_move(0, "O")
        move = self.ai.best_move(self.matrix)
        self.assertEqual(move, 0)

    def test_player_and_ai_turn(self):
        self.matrix.initialize_game()
        self.matrix.make_move(3, "X")
        ai_move = self.ai.best_move(self.matrix)
        self.matrix.make_move(ai_move, "O")
        moves = sum(
            cell != 0
            for row in self.matrix.grid
            for cell in row
        )
        self.assertEqual(moves, 2)

    def test_cannot_make_move_into_full_column(self):
        self.matrix.grid = [[0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0]]
        self.assertFalse(
            self.matrix.make_move(3, "X")
        )

    def test_current_board_state_changes(self):
        self.matrix.grid = [[0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0]]
        state1 = self.ai.current_board_state(self.matrix)
        self.matrix.make_move(0, "X")
        state2 = self.ai.current_board_state(self.matrix)
        self.assertNotEqual(state1, state2)

    def test_possible_moves_does_not_include_full_column(self):
        self.matrix.grid = [[0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0]]
        moves = self.ai.possible_moves(self.matrix)
        self.assertNotIn(3, moves)
