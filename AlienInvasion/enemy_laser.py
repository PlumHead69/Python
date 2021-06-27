import pygame

WHITE = (255, 255, 255)


class Enemy_Laser(pygame.sprite.Sprite):
   
    def __init__(self):
        
        super().__init__()

        self.image = pygame.image.load("enemy_laser.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 5

    def off(self):
        if self.rect.y < 580:
            return True
        else:
            return False
