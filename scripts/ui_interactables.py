import pygame

class UIInteractable:
    def __init__(self, game, interaction_name:str, interaction_type:str, pos:tuple, size:tuple):
        self.game = game
        self.interaction_name = interaction_name
        self.interaction_type = interaction_type
        self.pos = pos
        self.size = size

    def update(self, is_pressed=False):
        self.game.assets[self.interaction_name + '/' + self.interaction_type][is_pressed]

    def render(self, surf):
        surf.blit(self.update(), self.pos)

    def rect(self):
        return pygame.Rect(self.pos, self.size)

class ActionButton(UIInteractable):
    def __init__(self, game, interaction_name, pos, size):
        super().__init__(game, interaction_name, 'button', pos, size)

    def update(self, is_pressed=False):
        super().update(is_pressed)