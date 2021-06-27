import pygame

WHITE = (255, 255, 255)


class Ship(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [
                         0, 0, self.width, self.height])
