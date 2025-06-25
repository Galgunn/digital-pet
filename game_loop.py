import pygame, sys
from scripts.utils import *
from game_states.game import Game

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
            'tamagachi': load_images('tamagachi', None),
            'eat_buttons': load_images('eat_button', None),
            'play_buttons': load_images('play_button', None),
            'sleep_buttons': load_images('sleep_button', None),
            'ramiel_idle': Animation(load_images('ramiel/idle', None), 10)
        }

        self.load_state()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.interaction_options['spacebar'] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.interaction_options['spacebar'] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.interaction_options['left click'] = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.interaction_options['left click'] = False
            self.update()
            self.render()

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        self.state_stack[-1].render(self.display)
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.flip()
        self.clock.tick(60)

    def load_state(self):
        self.game_state = Game(self)
        self.state_stack.append(self.game_state)

    def reset_keys(self):
        for option in self.menu_options:
            self.menu_options[option] = False

if __name__ == '__main__':
    GameLoop().run()
        
