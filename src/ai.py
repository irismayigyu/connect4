import copy


class AI:
    '''Luokka, joka kuvaa tekoälyn toimintaa'''

    def __init__(self):
        self.best_moves = {}
        self.calculated_scores = {}

    def current_board_state(self, board):
        '''Tekee pelitilanteesta tuplen'''
        rows = []
        for row in board.grid:
            rows.append(tuple(row))
            return tuple(row)

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

    def evaluate(self, board, depth):
        '''Arvioi suopuisia tilanteita, ohjaa pelaaman keskisarakkeessa ja yrittämään voittaa pelin mahdollisimman aikaisin,
        korkeampi positiivinen arvo on hyvä Ai:lle'''
        score = 0
        if board.checker("O"):
            return 1000 + depth
        if board.checker("X"):
            return -1001 - depth
        center_points = 0
        for row in range(6):
            if board.grid[row][3] == "O":
                center_points += 1
        score += center_points * 6
        score += self.three_in_a_row(board, "O") * 10
        score -= self.three_in_a_row(board, "X") * 12
        return score

    def three_in_a_row(self, board, piece):
        "Kertoo kuinka monta tilannetta, jossa on kolme nappulaa peräkkäin"
        return (
            self.three_row(board, piece) +
            self.three_col(board, piece) +
            self.three_diag_down(board, piece) +
            self.three_diag_up(board, piece)
        )

    def three_row(self, board, piece):
        count = 0
        for row in board.grid:
            for col in range(7 - 2):
                if (row[col] == piece and
                    row[col+1] == piece and
                        row[col+2] == piece):
                    count += 1
        return count

    def three_col(self, board, piece):
        count = 0
        for col in range(7):
            for row in range(6 - 2):
                if (board.grid[row][col] == piece and
                    board.grid[row+1][col] == piece and
                        board.grid[row+2][col] == piece):
                    count += 1
        return count

    def three_diag_down(self, board, piece):
        count = 0
        for row in range(6 - 2):
            for col in range(7 - 2):
                if (board.grid[row][col] == piece and
                    board.grid[row+1][col+1] == piece and
                        board.grid[row+2][col+2] == piece):
                    count += 1
            return count

    def three_diag_up(self, board, piece):
        count = 0
        for row in range(2, 6):
            for col in range(7 - 2):
                if (board.grid[row][col] == piece and
                    board.grid[row-1][col+1] == piece and
                        board.grid[row-2][col+2] == piece):
                    count += 1
        return count

    def game_ended(self, board):
        '''Katsoo onko jompikumpi voittanut tai onko lauta täynnä'''
        return (
            board.checker("X")
            or board.checker("O")
            or board.full()
        )

    def minimax(self, board, depth, alpha, beta, maximizing):
        '''Valitsee AI-lle optimaalisen siirron pelaajaa vastaan. 
        AI on maksimoiva pelaaja ja vastustaja on minimoiva. 
        Alpha-beta pruning "leikkaa" pois ne vaihtoehdot, joita ei kannata valita ollenkaan, mikä nopeuttaa algoritmia.

        board: matrix-luokan olio 
        depth: miten pitkälle/syvälle simuloidaan eri pelisiirtovaihtoehtoja
        alpha: paras tähän asti löytynyt arvo maksimoivalle pelaajalle
        beta: paras tähän asti löytynyt arvo minimoivalle pelaajalle
        maximizing: kertoo kumpi pelaaja pelaa'''

        if depth == 0 or self.game_ended(board):
            return self.evaluate(board, depth)

        state = self.current_board_state(board)
        key = (state, depth, maximizing)
        if key in self.calculated_scores:
            return self.calculated_scores[key]
        if maximizing:
            best_score = -float("inf")
            best_move = None
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "O")
                score = self.minimax(new_board, depth-1, alpha, beta, False)
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            if best_move is not None:
                self.best_moves[state] = best_move
            self.calculated_scores[key] = best_score
            return best_score
        else:
            best_score = float("inf")
            best_move = None
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "X")
                score = self.minimax(new_board, depth-1, alpha, beta, True)
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            if best_move is not None:
                self.best_moves[state] = best_move
            self.calculated_scores[key] = best_score
            return best_score

    def best_move(self, board):
        '''Kutsuu best_move_at_depth -metodia eri syvyyksillä iteratiivisesti.
        Palauttaa parhaan syvimmän siirron'''
        self.best_moves = {}
        self.calculated_scores = {}
        best_col = None
        max_depth = 7
        for depth in range(1, max_depth + 1):
            move = self.best_move_at_depth(board, depth)
            if move is not None:
                best_col = move
        return best_col

    def best_move_at_depth(self, board, depth):
        '''Etsii parhaan siirron annetulla syvyydellä.
        Käyttää minimaxia simulointiin.
        Palauttaa parhaan siirron sille syvyydelle'''
        alpha = -float("inf")
        beta = float("inf")
        best_score = -float("inf")
        best_col = None
        for move in self.possible_moves(board):
            new_board = copy.deepcopy(board)
            new_board.make_move(move, "O")
            score = self.minimax(
                new_board,
                depth-1,
                alpha,
                beta,
                False
            )
            if score > best_score:
                best_score = score
                best_col = move
        return best_col
