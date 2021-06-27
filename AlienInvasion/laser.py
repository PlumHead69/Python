import pygame


WHITE = (255, 255, 255)

class Laser(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
 
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])

 
        #Initialise attributes of the car.
        
 
        # Draw the car (a rectangle!)
        #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
 
        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("enemy_laser.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.image = pygame.transform.rotate(self.image,90)
        self.image.set_colorkey(WHITE)

     

 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y-=8

    def off(self):
        if self.rect.y<=0:
            return True
    
    
