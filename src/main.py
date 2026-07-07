import sys
import pygame
from services.matrix import Matrix
from ui.gameview import Gameview


def init():
    '''Alustaa ikkunan ja kutsuu pelilooppia
'''
    pygame.init()
    pygame.display.set_caption("Connect 4")
    screen = pygame.display.set_mode((664, 584))
    matrix = Matrix()
    game = Gameview(screen, matrix)
    game.run_loop()


def quit_game():
    sys.exit()


if __name__ == "__main__":
    init()
