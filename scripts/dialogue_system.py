import pygame
from scripts.utils import FONT

class DialogueSystem:
    def __init__(self, game, lines:list):
        self.game = game
        self.dialogue_lines = lines
        self.font = FONT
        self.snip = self.font.render('', True, (255, 255, 255))
        self.counter = 0
        self.speed = 3
        self.line_done = False
        self.current_line = 0
        self.line = self.dialogue_lines[self.current_line]
        self.dialogue_complete = False

    def update(self):
        # Handles the type writer effect
        if self.counter < self.speed * len(self.line):
            self.counter += 1
        elif self.counter >= self.speed * len(self.line):
            self.line_done = True
        # Display line instantly
        if self.game.interaction_options['left click']['just pressed'] and not self.line_done: # Display current message instantly
            self.counter = self.speed * len(self.line)
        # Proceed to the next line
        elif self.game.interaction_options['left click']['just pressed'] and self.line_done and self.current_line < len(self.dialogue_lines) - 1: # Proceed to next line
            self.current_line += 1
            self.line_done = False
            self.line = self.dialogue_lines[self.current_line]
            self.counter = 0
        elif self.current_line == len(self.dialogue_lines) - 1 and self.line_done:
            self.dialogue_complete = True

        self.snip = self.font.render(self.line[0:self.counter//self.speed], True, 'white', None, 190)

    def render(self, surf, pos:tuple):
        surf.blit(self.snip, pos)

    def reset(self):
        self.counter = 0
        self.line_done = False
        self.current_line = 0
        self.line = self.dialogue_lines[self.current_line]
        self.dialogue_complete = False        
        self.snip = self.font.render('', True, (255, 255, 255))
