from scripts.state import State
import pygame

SCREEN_COOR = (48, 66)
CIRCLE_COLOR = (203, 219, 252)

class Game(State):
    def __init__(self, game):
        super().__init__(game)
        self.play_button_state = 0
        self.eat_button_state = 0
        self.sleep_button_state = 0

        self.play_button_rect = pygame.Rect(54, 174, 26, 28)
        self.eat_button_rect = pygame.Rect(91, 186, 26, 28)
        self.sleep_button_rect = pygame.Rect(128, 174, 26, 28)

        self.start = False

        self.circle_width = 75

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)
        if self.game.interaction_options['left click']: # left click is true
            if self.play_button_rect.collidepoint(mpos):
                self.play_button_state = 1
            if self.eat_button_rect.collidepoint(mpos):
                self.eat_button_state = 1
            if self.sleep_button_rect.collidepoint(mpos):
                self.sleep_button_state = 1
        if not self.game.interaction_options['left click']: # left click is false
            self.play_button_state = 0
            self.eat_button_state = 0
            self.sleep_button_state = 0
    
        if self.eat_button_state or self.play_button_state or self.sleep_button_state == 1:
            self.start = True
        
        if self.start:
            if self.circle_width != 5:
                self.circle_width -=1
            else:
                self.game.assets['ramiel_idle'].update()

    def render(self, surf):
        surf.fill((200, 30, 50))
        surf.blit(self.game.assets['tamagachi'][1], (0,0))
        surf.blit(self.game.assets['ramiel_idle'].img(), (48, 65))
        pygame.draw.circle(surf, CIRCLE_COLOR, (104, 109), 75, self.circle_width)
        surf.blit(self.game.assets['tamagachi'][0], (0,0))
        surf.blit(self.game.assets['play_buttons'][self.play_button_state], (0,0))
        surf.blit(self.game.assets['eat_buttons'][self.eat_button_state], (0,0))
        surf.blit(self.game.assets['sleep_buttons'][self.sleep_button_state], (0,0))