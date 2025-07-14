import pygame

class UIInteractable:
    def __init__(self, game, interaction_name:str, interaction_type:str, pos:tuple, size:tuple):
        self.game = game
        self.interaction_name = interaction_name
        self.interaction_type = interaction_type
        self.is_pressed = False
        self.just_pressed = False
        self.rect = pygame.Rect(pos, size)

    def update(self, mpos):
        self.is_pressed = False
        self.just_pressed = False

        if self.game.interaction_options['left click']['just pressed']: # left click is true
            if self.rect.collidepoint(mpos):
                self.just_pressed = True
        if self.game.interaction_options['left click']['held']: # left click is true
            if self.rect.collidepoint(mpos):
                self.is_pressed = True

    def render(self, surf):
        surf.blit(self.game.assets[self.interaction_name + '/' + self.interaction_type][self.is_pressed], (0,0))

class ActionButton(UIInteractable):
    def __init__(self, game, interaction_name, pos, size):
        super().__init__(game, interaction_name, 'button', pos, size)
