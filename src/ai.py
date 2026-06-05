
import copy


class AI:
    '''Luokka, joka kuvaa tekoälyn toimintaa'''

    def __init__(self):
        pass

    def possible_moves(self, board):
        '''Luo listan mahdollisista liikkeistä, joita voidaan tehdä eli jos sarake ei ole vielä täynnä
        tehostaakseen alpha-beta pruningia, sarakkeet ovat keskeltä reunoille'''
        moves = []
        for col in [3, 4, 2, 1, 5, 6, 0]:
            if board.grid[0][col] == 0:
                moves.append(col)
        return moves

    def evaluate(self, board, depth):
        '''Arvioi Ai:lle suopuisia tilanteita, ohjaa pelaaman keskisarakkeessa ja yrittämään voittaa pelin mahdollisimman aikaisin
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
        score += center_points * 9
        return score

    def game_ended(self, board):
        '''Katsoo onko jompikumpi voittanut tai onko lauta täynnä'''
        return (
            board.checker("X")
            or board.checker("O")
            or board.full()
        )

    def minimax(self, board, depth, alpha, beta, maximizing):
        '''mini-max algoritmi valitsee ai-lle optimaalisen siirron pelaajaa vastaan. 
        Ai on maksimoiva pelaaja ja vastustaja on minimoiva. alpha-beta pruning 
        "leikkaa" pois ne vaihtoehdot, joita ei kannata valita ollenkaan, mikä nopeuttaa algoritmia

        board: matrix-luokan olio 
        depth: miten pitkälle/syvälle simuloidaan eri pelisiirto vaihtoehtoja
        alpha: paras tähän asti löytynyt arvo maksimoivalle pelaajalle
        beta: paras tähän asti löytynyt arvo minimoivalle pelaajalle
        maximizing: kertoo kumpi pelaaja pelaa'''

        if depth == 0 or self.game_ended(board):
            return self.evaluate(board, depth)
        if maximizing:  # ai:n vuoro
            best_score = -float("inf")
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "O")
                score = self.minimax(new_board, depth-1, alpha, beta, False)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:  # toisen pelaajan vuoro
            best_score = float("inf")
            for move in self.possible_moves(board):
                new_board = copy.deepcopy(board)
                new_board.make_move(move, "X")
                score = self.minimax(new_board, depth-1, alpha, beta, True)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:  # muita vaihtoehtoja ei tarvii tutkia
                    break
            return best_score

    def best_move(self, board):
        '''Tarkistaa parasta siirtoa käyttäen minimaxia ja palauttaa parhaan kolumnin siirtoa varten'''
        alpha = -float("inf")
        beta = float("inf")
        best_score = -float("inf")
        best_col = None
        for move in self.possible_moves(board):
            new_board = copy.deepcopy(board)
            new_board.make_move(move, "O")
            score = self.minimax(
                new_board, 5, alpha, beta, False)
            if score > best_score:
                best_score = score
                best_col = move
        return best_col
