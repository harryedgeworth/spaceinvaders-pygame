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

    def movement(enemy_list, width = 800):
        if enemy_list[-1].rect.right >= width or enemy_list[0].rect.left <= 0:
            for i in enemy_list:
                i.speed *= -1
                i.rect.y += 25

    def spawnEnemyRow(enemy_list, height):
        x = 50
        for i in range(10):
            enemy_list.append(Enemy(x, height))
            x += 55
