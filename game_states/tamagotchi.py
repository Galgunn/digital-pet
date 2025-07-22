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
        self.button_just_pressed = [False, False, False]
        self.start = False
        self.circle_width = 75

        self.ramiel = Ramiel(self.game, (48, 65))
        self.play_button = ActionButton(self.game, 'play', (54, 174), (26, 28))
        self.eat_button = ActionButton(self.game, 'eat', (91, 186), (26, 28))
        self.sleep_button = ActionButton(self.game, 'sleep', (128, 174), (26, 28))
        self.dialogue_state = DialogBox(self.game)

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)

        self.play_button.update(mpos)
        self.eat_button.update(mpos)
        self.sleep_button.update(mpos)

        button_states = (self.play_button.just_pressed, self.eat_button.just_pressed, self.sleep_button.just_pressed)

        for x in range(len(button_states)):
            if button_states[x] == True:
                self.start = True

        if self.start:
            if self.circle_width != 5:
                self.circle_width -=1

            self.ramiel.update(button_states)

            if self.ramiel.animation_done:
                self.dialogue_state.enter_state()


    def render(self, surf):
        surf.fill((200, 30, 50))
        surf.blit(self.game.assets['tamagachi'][1], (0,0))
        self.ramiel.render(surf)
        pygame.draw.circle(surf, CIRCLE_COLOR, (104, 109), 75, self.circle_width)
        surf.blit(self.game.assets['tamagachi'][0], (0,0))
        self.play_button.render(surf)
        self.eat_button.render(surf)
        self.sleep_button.render(surf)