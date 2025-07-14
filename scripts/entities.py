import pygame

class Entity:
    def __init__(self, game, e_type, pos):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)

        # Animation
        self.action = ''
        self.set_action('idle')

    # def rect(self):
    #     return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action:str):
        if self.action != action:
            self.action = action
            self.animation = self.game.assets[self.e_type + '/' + self.action].copy()

    def update(self):
        self.animation.update()

    def render(self, surf):
        surf.blit(self.animation.img(), self.pos)

class Ramiel(Entity):
    def __init__(self, game, pos):
        super().__init__(game, 'ramiel', pos)
        self.starting_animation_done = False

    def update(self, button_pressed=(0, 0, 0)):
        super().update()
    
        if self.starting_animation_done:
            if button_pressed[0]:
                self.set_action('nod')
            if self.animation.done:
                self.animation_done()
                self.set_action('idle')
        else:
            self.set_action('idle')
            self.starting_animation_done = True

    def animation_done(self):
        current_animation_done = True