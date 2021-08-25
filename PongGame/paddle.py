import pygame as p

WHITE = (255, 255, 255)


class Paddle(p.sprite.Sprite):

    def __init__(self):

        super().__init__()

        
        image = p.image.load('rect.png')
        image = p.transform.scale(image, (40, 20))
        self.mask = p.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def moveUP(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def repaint(self, color):
        self.color = color
        p.draw.rect(self.image, self.color, [
                         0, 0, self.width, self.height])
