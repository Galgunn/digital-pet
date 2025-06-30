import pygame

class Entity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)
        self.size = size

        # Animation
        self.action = ''
        self.set_action('idle')

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action):
        if self.action != action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

    def update(self, button_pressed=(0, 0, 0)):
        self.button_pressed = button_pressed
        self.animation.update()

    def render(self, surf):
        surf.blit(self.animation.img(), self.pos)

class Ramiel(Entity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'ramiel', pos, size)

    def update(self, button_pressed=(0,0,0)):
        return super().update(button_pressed=button_pressed)
    

        
