

class Matrix:
    '''Luokka, joka kuvaa peliruudukkoa ja sen toimintaa

    Attributes: 
            grid: pelin ruudukko 6x7
            player: pelaaja, jonka vuoro on
    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa ruudukon

        _initialize_game(): funktio alustaa tyhjän matriisin
        '''

        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.player = "X"
        self.game_over = False
        self.game_won = False
        self._initialize_game()

    def _initialize_game(self):
        self.grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        return self.grid

    # def print_board(self):
    #     '''Komentorivi testausta varten, tulostaa pelilaudan ruudukkona terminaaliin'''

    #     print("\n  1 2 3 4 5 6 7")

    #     for row in self.grid:
    #         print("|", end="")
    #         for cell in row:
    #             if cell == 0:
    #                 print(" .", end="")
    #             else:
    #                 print(f" {cell}", end="")
    #         print(" |")
    #     print("-----------------\n")

    def make_move(self, col, player):
        for row in range(5, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return True
        return False

    def change_turns(self):
        self.player = "O" if self.player == "X" else "X"

    def checker(self, player):
        '''Luokan metodi, joka tarkistaa voittiko joku'''
        if self.row_check(player) or self.col_check(player) or self.diag_up_check(player) or self.diag_down_check(player):
            return True
        else:
            return False

    def row_check(self, player):
        for row in range(6):
            for col in range(4):
                if (self.grid[row][col] == player and
                    self.grid[row][col + 1] == player and
                    self.grid[row][col + 2] == player and
                        self.grid[row][col + 3] == player):
                    return True

    def col_check(self, player):
        for row in range(3):
            for col in range(7):

                if (self.grid[row][col] == player and
                    self.grid[row + 1][col] == player and
                    self.grid[row + 2][col] == player and
                        self.grid[row + 3][col] == player):

                    return True

    def diag_up_check(self, player):
        for row in range(3):
            for col in range(4):
                if (self.grid[row][col] == player and
                    self.grid[row + 1][col + 1] == player and
                    self.grid[row + 2][col + 2] == player and
                        self.grid[row + 3][col + 3] == player):
                    return True

    def diag_down_check(self, player):
        for row in range(3):
            for col in range(3, 7):
                if (self.grid[row][col] == player and
                    self.grid[row + 1][col - 1] == player and
                    self.grid[row + 2][col - 2] == player and
                        self.grid[row + 3][col - 3] == player):
                    return True

    def full(self):
        for row in self.grid:
            if 0 in row:
                return False

        return True
