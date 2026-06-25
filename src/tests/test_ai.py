import unittest
from services.matrix import Matrix
from ai import AI
import time


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

    def test_evaluate(self):

        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", 0, "O", "O", 0, 0, 0],
                            ["X", 0, "X", "O", 0, "O", "O"]]
        self.assertEqual(self.ai.evaluate(
            self.matrix), 130)

        self.matrix.grid = [[0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "O", 0, 0, 0, "O"],
                            [0, 0, "X", 0, 0, 0, "O"],
                            ["O", 0, "X", 0, 0, 0, "X"],
                            ["O", 0, "O", 0, 0, 0, "X"],
                            ["O", "O", "O", 0, 0, 0, "X"]]
        self.assertEqual(self.ai.evaluate(
            self.matrix), 150)

        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", "X", "O", 0, 0, 0, 0],
                            ["X", "X", "X", 0, "X", 0, 0]]
        self.assertEqual(self.ai.evaluate(
            self.matrix), -310)

    def test_three_in_row_window(self):
        window = ["O", "O", "O", 0]
        self.assertEqual(self.ai.evaluate_window(window, "O"), 50)

    def test_blocked_window(self):
        window = ["O", "O", "X", 0]
        self.assertEqual(self.ai.evaluate_window(window, "O"), 0)

    def test_best_move(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, "X", 0, 0, 0, 0],
                            ["O", 0, "X", 0, 0, 0, 0],
                            ["O", 0, "O", 0, 0, 0, 0],
                            ["O", "X", "X", "X", 0, 0, 0]]
        self.assertEqual(self.ai.best_move(self.matrix), 0)

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

    def test_player_and_ai_turns_works(self):
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

    def test_best_move_goes_first(self):
        self.matrix.initialize_game()
        state = self.ai.current_board_state(self.matrix)
        self.ai.best_moves[state] = 2
        moves = self.ai.possible_moves(self.matrix)
        self.assertEqual(moves[0], 2)

    def test_cannot_make_move_into_full_column(self):
        self.matrix.grid = [[0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0],
                            [0, 0, 0, "O", 0, 0, 0]]
        state = self.ai.current_board_state(self.matrix)
        self.ai.best_moves[state] = 3
        moves = self.ai.possible_moves(self.matrix)
        self.assertFalse(self.matrix.make_move(3, "X"))
        self.assertNotIn(3, moves)

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

    def test_minimax_finds_win_depth_1(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            ["X", 0, 0, "O", "O", "O", "X"]]
        score, move = self.ai.minimax(
            self.matrix,
            5,
            -float("inf"),
            float("inf"),
            True,
            time.time(),
            100,
            None, None, None
        )
        self.assertEqual(move, 2)
        self.assertEqual(score, 1004)

    def test_minimax_finds_win_depth_3(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            ["X", 0, 0, "O", 0, 0, "X"],
                            ["X", 0, 0, "O", "O", 0, "X"]]
        score, move = self.ai.minimax(
            self.matrix,
            5,
            -float("inf"),
            float("inf"),
            True,
            time.time(),
            100,
            None, None, None
        )
        self.assertEqual(move, 2)
        self.assertGreaterEqual(score, 1002)

    def test_minimax_doesnt_find_win_with_lower_depth(self):
        self.matrix.grid = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            ["X", 0, 0, "O", 0, 0, "X"],
                            ["X", 0, 0, "O", "O", 0, "X"]]
        score2, move2 = self.ai.minimax(
            self.matrix,
            2,
            -float("inf"),
            float("inf"),
            True,
            time.time(),
            100,
            None, None, None
        )
        self.assertLess(score2, 1000)
