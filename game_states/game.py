from scripts.state import State
from scripts.entities import Ramiel
from scripts.ui_interactables import ActionButton
from game_states.dialog_box import DialogBox
import pygame

SCREEN_COOR = (48, 66)
CIRCLE_COLOR = (203, 219, 252)

class Game(State):
    def __init__(self, game):
        super().__init__(game)
        self.button_states = [0, 0, 0]
        self.button_just_pressed = [False, False, False]

        self.play_button_rect = pygame.Rect(54, 174, 26, 28)
        self.eat_button_rect = pygame.Rect(91, 186, 26, 28)
        self.sleep_button_rect = pygame.Rect(128, 174, 26, 28)

        self.start = False

        self.circle_width = 75

        self.ramiel = Ramiel(self.game, (48, 65))
        self.play_button = ActionButton(self, 'play', (54, 174), (26, 28))

    def update(self):
        for x in range(3):
            self.button_states[x] = 0
            self.button_just_pressed[x] = False
        
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)

        if self.game.interaction_options['left click']['just pressed']:
            self.start = True
            if self.play_button_rect.collidepoint(mpos):
                self.button_just_pressed[0] = True
        # if self.ramiel.animation_done():
        #     print('done')
                    # DialogBox(self.game).enter_state()

        if self.game.interaction_options['left click']['held']: # left click is true
            if self.play_button_rect.collidepoint(mpos):
                self.button_states[0] = 1
            if self.eat_button_rect.collidepoint(mpos):
                self.button_states[1] = 1
            if self.sleep_button_rect.collidepoint(mpos):
                self.button_states[2] = 1

        if self.start:
            if self.circle_width != 5:
                self.circle_width -=1
            self.ramiel.update(self.button_just_pressed)

    def render(self, surf):
        surf.fill((200, 30, 50))
        surf.blit(self.game.assets['tamagachi'][1], (0,0))
        self.ramiel.render(surf)
        pygame.draw.circle(surf, CIRCLE_COLOR, (104, 109), 75, self.circle_width)
        surf.blit(self.game.assets['tamagachi'][0], (0,0))
        surf.blit(self.game.assets['play_buttons'][self.button_states[0]], (0,0))
        surf.blit(self.game.assets['eat_buttons'][self.button_states[1]], (0,0))
        surf.blit(self.game.assets['sleep_buttons'][self.button_states[2]], (0,0))