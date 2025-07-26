import json
import pygame
from scripts.state import State
from scripts.dialogue_system import DialogueSystem

BASE_JSON_PATH = 'assets/dialogue/'

class DialogBox(State):
    def __init__(self, game, dialogue_key:str, filename:str):
        super().__init__(game)
        self.dialogue_dict = {}
        self.json_filename = filename
        self.load('assets/dialogue/play_button.json')
        self.lines = self.dialogue_dict[dialogue_key]
        self.dialogue_system = DialogueSystem(self.game, self.lines)
        self.rect = pygame.Rect(0, 170, 250, 100)

    def on_enter(self):
        self.dialogue_system.reset()
        self.load(BASE_JSON_PATH + self.json_filename)

    def update(self):
        self.prev_state.update_animation() # type: ignore error due to prev state being None
        self.dialogue_system.update()

        if self.game.interaction_options['left click']['just pressed'] and self.dialogue_system.dialogue_complete:
            self.exit_state()

    def render(self, surf):
        self.prev_state.render(surf) # type: ignore error due to prev state being None
        pygame.draw.rect(surf, ('black'), self.rect)
        self.dialogue_system.render(surf, (self.rect.x + 10, self.rect.y + 10))

    def enter_state(self):
        super().enter_state()

    def exit_state(self):
        super().exit_state()

    def load(self, path):
        f = open(path, 'r')
        dialogue_data = json.load(f)
        f.close()

        self.dialogue_dict = dialogue_data
