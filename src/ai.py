
import copy


class AI:
    '''Luokka, joka kuvaa tekoälyn toimintaa'''

    def __init__(self):
        pass

    def possible_moves(self, board):
        moves = []
        for col in range(7):
            if board.grid[0][col] == 0:
                moves.append(col)
        return moves

    def evaluate(self, board):
        '''Arvioi Ai:lle suopuisia tilanteita, ohjaa pelaaman keskisarakkeessa'''
        score = 0
        if board.checker("O"):
            return 1000
        if board.checker("X"):
            return -1001
        center_points = 0
        for row in range(6):
            if board.grid[row][3] == "O":
                center_points += 1
        score += center_points * 9
        return score

    def game_ended(self, board):
        return (
            board.checker("X")
            or board.checker("O")
            or board.full()
        )

    def minimax(self, board, depth, maximizing):
        if depth == 0 or self.game_ended(board):
            return self.evaluate(board)
        if maximizing:
            best_score = -float("inf")
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "O")
                score = self.minimax(new_board, depth-1, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "X")
                score = self.minimax(new_board, depth-1, True)
                best_score = min(best_score, score)
            return best_score

    def best_move(self, board):
        best_score = -float("inf")
        best_col = None
        for move in self.possible_moves(board):
            new_board = copy.deepcopy(board)
            new_board.make_move(move, "O")
            score = self.minimax(new_board, 4, False)
            if score > best_score:
                best_score = score
                best_col = move
        return best_col
