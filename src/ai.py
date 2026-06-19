import copy
import time


class AI:
    '''Luokka, joka kuvaa tekoälyn toimintaa'''

    def __init__(self):
        self.best_moves = {}

    def current_board_state(self, board):
        '''Tekee pelitilanteesta tuplen'''
        return tuple(tuple(row) for row in board.grid)

    def possible_moves(self, board):
        '''Luo listan mahdollisista siirroista.
        Sarakkeet ovat järjestyksessä keskeltä reunoille,
        Tarkistaa onko tilanteeseen aikaisemmin laskettu jo hyvä siirto, jos kyllä niin 
        siirtää tämän siirron listan eteen'''
        moves = []
        for col in [3, 4, 2, 1, 5, 6, 0]:
            if board.grid[0][col] == 0:
                moves.append(col)
        state = self.current_board_state(board)
        if state in self.best_moves:
            best = self.best_moves[state]
            if best in moves:
                moves.remove(best)
                moves.insert(0, best)
        return moves

    def evaluate(self, board):
        '''Heuristiikkafunktio arvioi suopuisia tilanteita 
        neljän ikkunoiden avulla.
        Korkeampi positiivinen arvo on hyvä Ai:lle'''
        score = 0
        for row in range(6):
            for col in range(7 - 3):
                window = [board.grid[row][col + i] for i in range(4)]
                score += self.evaluate_window(window, "O")
                score -= self.evaluate_window(window, "X")
        for col in range(7):
            for row in range(6 - 3):
                window = [board.grid[row + i][col] for i in range(4)]
                score += self.evaluate_window(window, "O")
                score -= self.evaluate_window(window, "X")
        for row in range(6 - 3):
            for col in range(7 - 3):
                window = [board.grid[row + i][col + i] for i in range(4)]
                score += self.evaluate_window(window, "O")
                score -= self.evaluate_window(window, "X")
        for row in range(3, 6):
            for col in range(7 - 3):
                window = [board.grid[row - i][col + i] for i in range(4)]
                score += self.evaluate_window(window, "O")
                score -= self.evaluate_window(window, "X")
        return score

    def evaluate_window(self, window, player):
        '''Arvioi ikkunoiden tilanteita ja antaa sen mukaan pisteitä'''
        opp = "X" if player == "O" else "O"
        if player in window and opp in window:
            return 0

        if window.count(player) == 4:
            return 1000
        if window.count(player) == 3 and window.count(0) == 1:
            return 50
        if window.count(player) == 2 and window.count(0) == 2:
            return 10
        if window.count(opp) == 3 and window.count(0) == 1:
            return -70
        if window.count(opp) == 2 and window.count(0) == 2:
            return -10
        return 0

    def best_move(self, board):
        '''Kutsuu minimaxia iteratiivisesti niin syvälle kun kerkeää 
        kunnes tulee aikakatkaisu ja palauttaa siihen asti saadun parhaan siirron'''
        best_col = None
        start_time = time.time()
        time_limit = 1
        depth = 1
        while True:
            if time.time() - start_time > time_limit:
                break
            try:
                score, move = self.minimax(
                    board,
                    depth,
                    -float("inf"),
                    float("inf"),
                    True,
                    start_time,
                    time_limit, None, None, None
                )
                if move is not None:
                    best_col = move
            except TimeoutError:
                break
            depth += 1
        return best_col

    def minimax(self, board, depth, alpha, beta, maximizing, start_time, time_limit, last_row,
                last_col,
                last_player):
        '''Valitsee AI-lle optimaalisen siirron pelaajaa vastaan.
        AI on maksimoiva pelaaja ja vastustaja on minimoiva.
        Alpha-beta pruning "leikkaa" pois ne vaihtoehdot,
        joita ei kannata valita ollenkaan, mikä nopeuttaa algoritmia.

        board: matrix-luokan olio
        depth: miten pitkälle/syvälle simuloidaan eri pelisiirtovaihtoehtoja
        alpha: paras tähän asti löytynyt arvo maksimoivalle pelaajalle
        beta: paras tähän asti löytynyt arvo minimoivalle pelaajalle
        maximizing: kertoo kumpi pelaaja pelaa'''
        if time.time() - start_time > time_limit:
            raise TimeoutError
        if last_row is not None:
            if board.checker(last_row, last_col, last_player):
                if last_player == "O":
                    return 1000 + depth, None
                return -1000 - depth, None
        if board.full():
            return 0, None
        if depth == 0:
            return self.evaluate(board), None
        state = self.current_board_state(board)

        if maximizing:
            best_score = -float("inf")
            best_move = None
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                row, col = new_board.make_move(move, "O")
                score, _ = self.minimax(new_board, depth - 1, alpha, beta,
                                        False, start_time, time_limit, row, col, "O"
                                        )
                if score > best_score:
                    best_score = score
                    best_move = move
                    alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            self.best_moves[state] = best_move
            return best_score, best_move

        best_score = float("inf")
        best_move = None
        for move in self.possible_moves(board):
            new_board = copy.deepcopy(board)
            row, col = new_board.make_move(move, "X")
            score, _ = self.minimax(new_board, depth - 1, alpha,
                                    beta, True, start_time, time_limit, row, col, "X"
                                    )
            if score < best_score:
                best_score = score
                best_move = move
                beta = min(beta, best_score)
            if beta <= alpha:
                break
        self.best_moves[state] = best_move
        return best_score, best_move
