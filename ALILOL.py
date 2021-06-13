import pygame


pygame.init()

class Ship:
    def __init__(self,x,y):
        self.pos_x=x
        self.pos_y=y

    def left(self):
        self.pos_x-=30
    def right(self):
        self.pos_x+=30
    def draw(self):
        gameDisplay.blit(shipImg,(self.pos_x,self.pos_y))

 


class Laser:
    def __init__(self,x,y):
        self.pos_x=x
        self.pos_y=y
        
    def update(self):
        self.pos_y-=1

    def off(self):
        return self.pos_y<=0

    def draw(self):
        gameDisplay.blit(laserImg,(self.pos_x,self.pos_y))


class Alien:
    def __init__(self,x,y):
       self.pos_x=x
       self.pos_y=y
       self.direction="right"

    def update(self):
        if self.direction=="right":
            self.pos_x+=1
            if self.pos_x==740:
                self.pos_y+=10
                self.direction="left"
        if self.direction=="left":
            self.pos_x-=1
            if self.pos_x==0:
                self.pos_y+=10
                self.direction="right"
        if self.pos_y==450:
            self.direction=None


    def draw(self):
        gameDisplay.blit(alienImg,(self.pos_x,self.pos_y))






alien=Alien(0,0)
alien_2=Alien(100,0)
alien_3=Alien(200,0)
aliens=[]
aliens.append(alien)
aliens.append(alien_2)
aliens.append(alien_3)



display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))


black = (0,0,0)
white = (255,255,255)

ship=Ship(400,500)
laser=None

crashed = False
shipImg = pygame.image.load('spaceship.png').convert()
alienImg=pygame.image.load("alien.png").convert()
bc_Img=pygame.image.load("space.jpg").convert()
shipImg.set_colorkey(black)

laserImg=pygame.image.load("laser.png").convert()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
        if event.type == pygame.KEYDOWN:
            key = event.dict["key"]
            if key == ord("a"):
                ship.left()    
            elif key == ord("d"):
                ship.right()     
            elif key == ord("w") and laser==None :
                laser=Laser(ship.pos_x,ship.pos_y)
                
    gameDisplay.blit(bc_Img, [0, 0])    
        
    ship.draw()
    
    for alien in aliens:
        alien.draw()
        alien.update()
    
    
    if laser!=None:
        laser.draw()
        laser.update()
        if laser.off():
            laser=None



    
        
    pygame.display.flip()
    

pygame.quit()
quit()


#valtoztatas

#fasz













