import pygame
from ai import AI


class Pelinäkymä:
    '''Luokka, jolla piirretään pelinäkymä'''

    def __init__(self, screen, matrix):
        '''Luokan konstruktori, jolla alustetaan pelinäkymä ja luokan argumentit

        Args:
        matrix: peliruudukko, Matrix-luokan olio
        gap: ruudukon ruutujen välissä oleva väli
        ai: AI-luokan olio
        '''
        self.matrix = matrix
        self.ai = AI()
        self.font = pygame.font.SysFont("Comic Sans", 17)
        self.screen = screen
        self.cell_size = 90
        self.gap = 3
        self.winner = None

    def run_loop(self):
        '''Pelilooppi'''

        is_running = True
        while is_running:
            self.screen.fill((125, 158, 192))
            self.draw_circles()
            if self.matrix.game_over:
                self.announce_winner(self.winner)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.matrix.game_over:
                    x = event.pos[0]
                    col = x // 80
                    col = (x - 20) // (self.cell_size + self.gap)
                    if 0 <= col <= 6:
                        self.matrix.make_move(col, "X")
                    if self.matrix.checker("X"):
                        self.winner = "X"
                        self.matrix.game_over = True
                    else:
                        self.matrix.change_turns()
                        self.ai_turn()
                    if self.matrix.full():
                        self.winner = "Draw"
                        self.matrix.game_over = True

    def ai_turn(self):
        ai_col = self.ai.best_move(self.matrix)
        if ai_col is not None:
            self.matrix.make_move(ai_col, "O")
            if self.matrix.checker("O"):
                self.winner = "O"
                self.matrix.game_over = True
            else:
                self.matrix.change_turns()

    def announce_winner(self, player):
        winner_message = self.font.render(
            f"{player} has won!", True, (0, 0, 0))
        self.screen.blit(winner_message, (34, 160))

    def draw_circles(self):
        for row in range(6):
            for col in range(7):
                x = col * (self.cell_size + self.gap) + 10
                y = row * (self.cell_size + self.gap) + 10
                value = self.matrix.grid[row][col]
                if value == "X":
                    color = (255, 0, 0)
                elif value == "O":
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)
                pygame.draw.circle(
                    self.screen,
                    color,
                    (x + self.cell_size // 2, y + self.cell_size // 2),
                    35
                )
