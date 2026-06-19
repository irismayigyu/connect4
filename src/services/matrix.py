'''Sisältää pelin logiikan ja Matrix-luokan'''


class Matrix:
    '''Luokka, joka kuvaa peliruudukkoa ja sen toimintaa

    Attributes: 
            grid: pelin ruudukko 6x7
            player: pelaaja, jonka vuoro on
    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa ruudukon

        initialize_game(): funktio alustaa tyhjän matriisin
        '''

        self.player = "X"
        self.game_over = False
        self.game_won = False
        self.initialize_game()

    def initialize_game(self):
        self.grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        return self.grid

    def make_move(self, col, player):
        for row in range(5, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return row, col
        return None

    def change_turns(self):
        self.player = "O" if self.player == "X" else "X"

    def checker(self, row, col, player):
        '''Luokan metodi, joka tarkistaa voittiko joku viimeisimmän siirron perusteella'''
        if (
            self.row_check(row, col, player)
            or self.col_check(row, col, player)
            or self.diag_up_check(row, col, player)
            or self.diag_down_check(row, col, player)
        ):
            return True
        return False

    def row_check(self, row, col, player):
        '''Tarkistaa onko voittorivejä viimeisimmän nappulan vasemmalta (prev) 
        ja oikealta puolelta (next).
        Jos löytyyy neljä peräkkäistä palauttaa True'''
        count = 1
        prev_col = col - 1
        while prev_col >= 0 and self.grid[row][prev_col] == player:
            count += 1
            prev_col -= 1

        next_col = col + 1
        while next_col < 7 and self.grid[row][next_col] == player:
            count += 1
            next_col += 1
        if count >= 4:
            return True
        return False

    def col_check(self, row, col, player):
        '''Tarkistaa että onko viimeinen siirto tehnyt voiton tarkistamalla nappulan alhaalla
        olevia nappuloita'''
        count = 1
        next_row = row + 1
        while next_row < 6 and self.grid[next_row][col] == player:
            count += 1
            next_row += 1
        if count >= 4:
            return True
        return False

    def diag_up_check(self, row, col, player):
        '''Vasemmalta ylöspäin menevä rivi'''
        count = 1
        next_row, next_col = row + 1, col - 1
        while next_row < 6 and next_col >= 0 and self.grid[next_row][next_col] == player:
            count += 1
            next_row += 1
            next_col -= 1

        next_row, next_col = row - 1, col + 1
        while next_row >= 0 and next_col < 7 and self.grid[next_row][next_col] == player:
            count += 1
            next_row -= 1
            next_col += 1
        if count >= 4:
            return True
        return False

    def diag_down_check(self, row, col, player):
        '''Vasemmalta alaspäin'''
        count = 1
        next_row, next_col = row - 1, col - 1
        while next_row >= 0 and next_col >= 0 and self.grid[next_row][next_col] == player:
            count += 1
            next_row -= 1
            next_col -= 1

        next_row, next_col = row + 1, col + 1
        while next_row < 6 and next_col < 7 and self.grid[next_row][next_col] == player:
            count += 1
            next_row += 1
            next_col += 1
        if count >= 4:
            return True
        return False

    def full(self):
        for row in self.grid:
            if 0 in row:
                return False

        return True
