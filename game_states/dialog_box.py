import pygame
from scripts.state import State

class DialogBox(State):
    def __init__(self, game):
        super().__init__(game)
        self.lines = [
            'this is a message gng'
        ]

        self.font = pygame.font.SysFont('engravers', 12)
        self.snip = self.font.render('', True, (255, 255, 255))
        self.counter = 0
        self.speed = 3
        self.done = False
        self.current_line = 0
        self.line = self.lines[self.current_line]

    def update(self):
        if self.counter < self.speed * len(self.line):
            self.counter += 1
        elif self.counter >= self.speed * len(self.line):
            self.done = True

        if self.game.interaction_options['left click']['just pressed'] and not self.done: # Display current message instantly
            pass
            # self.counter = self.speed * len(self.line)
        elif self.game.interaction_options['left click']['just pressed'] and self.done and self.current_line < len(self.lines) - 1: # Proceed to next line
            self.current_line += 1
            self.done = False
            self.line = self.lines[self.current_line]
            self.counter = 0

        self.snip = self.font.render(self.line[0:self.counter//self.speed], True, 'white')
        self.game.reset_keys()

    def render(self, surf):
        surf.blit(self.snip, (10, 10))
