import pygame

WHITE = (255, 255, 255)


class Alien(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.direction = "right"

        self.image = pygame.image.load("alien.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        if self.direction == "right":
            self.rect.x += 5
            if self.rect.x == 740:
                self.rect.y += 30
                self.direction = "left"
        if self.direction == "left":
            self.rect.x -= 5
            if self.rect.x == 20:
                self.rect.y += 30
                self.direction = "right"
        if self.rect.y == 450:
            self.direction = None
