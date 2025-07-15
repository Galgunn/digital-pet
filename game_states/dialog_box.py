import pygame
from scripts.state import State

class DialogBox(State):
    def __init__(self, game):
        super().__init__(game)
        self.lines = [
            'this is a message gng',
            'another message',
            'and another'
        ]

        self.font = pygame.font.SysFont('engravers', 12)
        self.snip = self.font.render('', True, (255, 255, 255))
        self.counter = 0
        self.speed = 3
        self.line_done = False
        self.current_line = 0
        self.line = self.lines[self.current_line]
        self.dialogue_complete = False

    def update(self):
        if self.game.interaction_options['left click']['just pressed'] and self.dialogue_complete:
            self.counter = 0
            self.line_done = False
            self.current_line = 0
            self.line = self.lines[self.current_line]
            self.dialogue_complete = False
            self.exit_state()
        else:
            if self.counter < self.speed * len(self.line):
                self.counter += 1
            elif self.counter >= self.speed * len(self.line):
                self.line_done = True

            if self.current_line == len(self.lines) - 1 and self.line_done:
                self.dialogue_complete = True
            elif self.game.interaction_options['left click']['just pressed'] and not self.line_done: # Display current message instantly
                self.counter = self.speed * len(self.line)
            elif self.game.interaction_options['left click']['just pressed'] and self.line_done and self.current_line < len(self.lines) - 1: # Proceed to next line
                self.current_line += 1
                self.line_done = False
                self.line = self.lines[self.current_line]
                self.counter = 0

        self.snip = self.font.render(self.line[0:self.counter//self.speed], True, 'white')

    def render(self, surf):
        surf.blit('red')
        surf.blit(self.snip, (10, 10))
