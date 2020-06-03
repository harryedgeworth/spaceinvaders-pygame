import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.color = (255, 0, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.speed = 2 
        
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += self.speed

    def movement(enemyGroup):
        if enemyGroup[-1].rect.right >= 800 or enemyGroup[0].rect.left <= 0:
            for i in enemyGroup:
                i.speed *= -1
                i.rect.y += 25
