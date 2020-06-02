import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((90,15))
        self.color = (0, 0, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.speed = 0
        
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += self.speed

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= 800:
            self.rect.right = 800
