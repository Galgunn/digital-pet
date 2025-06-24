import pygame
from scripts.utils import *

pygame.init()

class GameLoop:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Oh yeah the game is just starting!!')
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.running = True

        self.state_stack = []
        self.interaction_options = {
            'left click': False,
            'spacebar': False
        }

        self.assets = {
            'tamagachi': None
        }
