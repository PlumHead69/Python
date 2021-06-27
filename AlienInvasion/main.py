import pygame, random
rng=random.Random()
from car import Car
from alien import Alien
from laser import Laser
from enemy_laser import Enemy_Laser
import math
matek=math
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
 
SCREENWIDTH=820
SCREENHEIGHT=580
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Alien invasion")
bc_Img=pygame.image.load("space.jpg").convert_alpha()

#text on screen
endings=["Good job commander!","WIN","U killed all of them!","f aliens","apa kínoz"]

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(rng.choice(endings), True, green)
textRect = text.get_rect()
textRect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)



e_laser=Enemy_Laser()
laser=Laser()
bullets_group = pygame.sprite.Group()
random_alien_list=[]

playerShip = Car()
playerShip.rect.x = 390
playerShip.rect.y = SCREENHEIGHT - 100

alien1=Alien()
alien1.rect.x=300
random_alien_list.append(alien1)

alien2=Alien()
alien2.rect.x=100
random_alien_list.append(alien2)

alien3=Alien()
alien3.rect.x=200
random_alien_list.append(alien3)

alien4=Alien()
alien4.rect.x=400
random_alien_list.append(alien4)

alien5=Alien()
alien5.rect.x=500
random_alien_list.append(alien5)

alien6=Alien()
alien6.rect.x=600
random_alien_list.append(alien6)

ship_sprites_list = pygame.sprite.Group()
ship_sprites_list.add(playerShip)

aliens_sprites_list = pygame.sprite.Group()
aliens_sprites_list.add(alien1)
aliens_sprites_list.add(alien2)
aliens_sprites_list.add(alien3)
aliens_sprites_list.add(alien4)
aliens_sprites_list.add(alien5)
aliens_sprites_list.add(alien6)


only_1_alien="okés"

i=0
carryOn = True

clock=pygame.time.Clock()
e_laser_timer=pygame.time.get_ticks()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     playerShip.moveRight(10)
        if alien6.rect.y==450 or alien5.rect.y==450 or alien4.rect.y==450 or alien3.rect.y==450 or alien2.rect.y==450 or alien1.rect.y==450:
            carryOn=False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerShip.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerShip.moveRight(5)
           
        if len(random_alien_list)==0:
           
            carryOn=False
        elif e_laser.off()==True and only_1_alien=="okés":
            e_laser.rect.x=rng.choice(random_alien_list).rect.x+45
            e_laser.rect.y=rng.choice(random_alien_list).rect.y
            bullets_group.add(e_laser)
            only_1_alien="nem okés"
        if keys[pygame.K_UP] and laser.off()==True:
            laser.rect.x=playerShip.rect.x+45
            laser.rect.y=playerShip.rect.y
            bullets_group.add(laser)
 
 
        hit_collision = pygame.sprite.spritecollide(laser,aliens_sprites_list,False)
        for alien_hitted in hit_collision:
            i+=1
            aliens_sprites_list.remove(alien_hitted)
            random_alien_list.remove(alien_hitted)
            

        ship_collision = pygame.sprite.spritecollide(e_laser,ship_sprites_list,False)
        for alien_hitted in ship_collision:
            carryOn=False
            
            
  
            
        
        screen.blit(bc_Img,[0,0])
        if i==6:
           screen.blit(text, textRect)

        
        
        if laser.off()==False:
            bullets_group.remove(laser)
            
        
        if e_laser.off()==False:
            bullets_group.remove(e_laser)
            e_laser.rect.y=0
            only_1_alien="okés"

        ship_sprites_list.draw(screen)
        ship_sprites_list.update()
        bullets_group.draw(screen)
        bullets_group.update()
        aliens_sprites_list.draw(screen)
        aliens_sprites_list.update()
       
        pygame.display.flip()
 
        clock.tick(60)
 
pygame.quit()
