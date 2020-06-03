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

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.change_state('menu')
                if event.key == pygame.K_LEFT:
                    self.player.speed -= 7
                if event.key == pygame.K_RIGHT:
                    self.player.speed += 7
                if event.key == pygame.K_SPACE:
                    print('fire')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.speed += 7
                if event.key == pygame.K_RIGHT:
                    self.player.speed -= 7

    def tick(self, clock):
        self.all_sprites.update()

        for enemies in self.enemies:
            Enemy.movement(enemies, self.width)

    def blit(self, surface):
        surface.fill((0, 0, 0))
        self.all_sprites.draw(surface)

    def join(self, old_state = None):
        if old_state == 'menu':
            self.player = Player(self.width // 2, self.height - 20)
            self.enemies = [
                [],
                [],
                [],
                [],
            ]

            x = 100
            
            for enemies in self.enemies:
                Enemy.spawnEnemyRow(enemies, x)
                x += 50

            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.player, self.enemies)
