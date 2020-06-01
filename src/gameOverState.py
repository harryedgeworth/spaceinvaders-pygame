from src.state import State

import pygame

class GameOverState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()

        def handleEvents(self, events):
            pass

        def tick(self, clock):
            pass

        def blit(self, surface):
            pass

        def join(self, old_state = None):
            pass
