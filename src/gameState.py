from src.state import State
from src.player import Player 
from src.enemy import Enemy

import pygame
import sys

class GameState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Game state here', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.width // 2, self.height // 2)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.change_state('menu')
                if event.key == pygame.K_LEFT:
                    self.player.speed -= 7
                if event.key == pygame.K_RIGHT:
                    self.player.speed += 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.speed += 7
                if event.key == pygame.K_RIGHT:
                    self.player.speed -= 7

    def tick(self, clock):
        self.all_sprites.update()

        if self.enemies[-1].rect.right >= self.width or self.enemies[0].rect.left <= 0:
            for i in self.enemies:
                i.speed *= -1
                i.rect.y += 25

    def blit(self, surface):
        surface.fill((255, 255, 255))
        self.all_sprites.draw(surface)

    def join(self, old_state = None):
        if old_state == 'menu':
            self.player = Player(self.width // 2, self.height - 20)
            
            x = 50 
            self.enemies = []
            for i in range(10):
                self.enemies.append(Enemy(x, 100))
                x += 55

            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.player, self.enemies)
