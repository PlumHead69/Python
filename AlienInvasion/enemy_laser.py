import pygame


WHITE = (255, 255, 255)

class Enemy_Laser(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
 
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("enemy_laser.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.image = pygame.transform.rotate(self.image,90)
        self.image.set_colorkey(WHITE)

     

 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y+=5

    def off(self):
        if self.rect.y<580:
            return True
        else:
            return False
        

    


    
    