from src.state import State

import pygame
import sys

class MenuState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Space Invaders', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.width // 2, self.height // 2)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    self.stateManager.change_state('game')

    def tick(self, clock):
        pass

    def blit(self, surface):
        surface.fill((255, 255, 255))
        surface.blit(self.text, self.textRect)
