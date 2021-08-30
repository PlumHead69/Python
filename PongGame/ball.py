import pygame as p

WHITE = (255, 255, 255)


class Ball(p.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = p.image.load("ball.png").convert_alpha()
        self.image = p.transform.scale(self.image, (30, 30))
        self.mask = p.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def repaint(self, color):
        self.color = color
        p.draw.rect(self.image, self.color, [
                         0, 0, self.width, self.height])

    def setx(self,number):
        self.number = number
        self.rect.x+= self.number
        return self.rect.x

    def sety(self,number):
        self.number = number
        self.rect.y+= self.number