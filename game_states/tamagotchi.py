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
        self.start = False
        self.start_animation_done = False
        self.circle_width = 75

        self.ramiel = Ramiel(self.game, (48, 65))
        self.play_button = ActionButton(self.game, 'play', (54, 174), (26, 28))
        self.eat_button = ActionButton(self.game, 'eat', (91, 186), (26, 28))
        self.sleep_button = ActionButton(self.game, 'sleep', (128, 174), (26, 28))

        self.pressed_counter = {
            'play': 0,
            'eat': 0,
            'sleep': 0,
        }

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)

        self.play_button.update(mpos)
        self.eat_button.update(mpos)
        self.sleep_button.update(mpos)

        if not self.start and (self.play_button.just_pressed or self.eat_button.just_pressed or self.sleep_button.just_pressed):
            self.start = True

        if self.start and not self.start_animation_done:
            if self.circle_width != 5:
                self.circle_width -=1
            else:
                self.start_animation_done = True
        elif self.start_animation_done:
            if self.play_button.just_pressed:
                self.json_file = 'play_button.json'
                self.dict_key = 'play'
                self.ramiel.set_action('nod')
            elif self.eat_button.just_pressed:
                self.json_file = 'eat_button.json'
                self.dict_key = 'eat'
                self.ramiel.set_action('nod')
            elif self.sleep_button.just_pressed:
                self.json_file = 'sleep_button.json'
                self.dict_key = 'sleep'
                self.ramiel.set_action('nod')

            if self.ramiel.animation_done:
                self.trigger_button_dialogue(self.json_file, self.dict_key, self.pressed_counter[self.dict_key])
                self.pressed_counter[self.dict_key] += 1

        self.ramiel.update()

    def update_animation(self):
        self.ramiel.update()

    def trigger_dialogue(self, json_file, dict_key):
        dilogue_state = DialogBox(self.game, dict_key, json_file)
        dilogue_state.enter_state()

    def trigger_button_dialogue(self, json_file, dict_key, index):
        index = (index % 3)
        dict_key = str(dict_key) + '_' + str(index)
        dialogue_state = DialogBox(self.game, dict_key, json_file)
        dialogue_state.enter_state()

    def render(self, surf):
        surf.fill((200, 30, 50))
        surf.blit(self.game.assets['tamagachi'][1], (0,0))
        self.ramiel.render(surf)
        pygame.draw.circle(surf, CIRCLE_COLOR, (104, 109), 75, self.circle_width)
        surf.blit(self.game.assets['tamagachi'][0], (0,0))
        self.play_button.render(surf)
        self.eat_button.render(surf)
        self.sleep_button.render(surf)