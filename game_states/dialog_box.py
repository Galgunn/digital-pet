import pygame
from scripts.state import State
from scripts.dialogue_system import DialogueSystem

class DialogBox(State):
    def __init__(self, game):
        super().__init__(game)
        self.lines = [
            'this is a message gng',
            'another message',
            'and another'
        ]
        self.dialogue_system = DialogueSystem(self.game, self.lines)
        self.rect = pygame.Rect(0, 170, 250, 100)

    def on_enter(self):
        self.dialogue_system.reset()

    def update(self):
        self.prev_state.update_animation() # type: ignore error due to prev state being None
        self.dialogue_system.update()

        if self.game.interaction_options['left click']['just pressed'] and self.dialogue_system.dialogue_complete:
            self.exit_state()

    def render(self, surf):
        self.prev_state.render(surf) # type: ignore error due to prev state being None
        pygame.draw.rect(surf, ('black'), self.rect)
        self.dialogue_system.render(surf, (self.rect.x + 10, self.rect.y + 10))

    def exit_state(self):
        self.dialogue_system.reset()
        super().exit_state()
