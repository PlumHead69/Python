import pygame as p
import random
import time
from paddle import Paddle
from ball import Ball

p.init()

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

DisplayScreen = p.display.set_mode((display_width, display_height))
p.display.set_caption('PongGame')

ball=Ball()

Paddle_a=Paddle()
Paddle_a.rect.x = 50
Paddle_a.rect.y=400

Paddle_b=Paddle()
Paddle_b.rect.x = 550
Paddle_b.rect.y=400


paddle_list = p.sprite.Group()
paddle_list.add(Paddle_a)
paddle_list.add(Paddle_b)

gameFinish=True
DisplayScreen.fill(color_black)
while gameFinish==True:

    for anyEvent in p.event.get():
        if anyEvent.type == p.QUIT:
            gameFinish = False
    if anyEvent.type == p.KEYDOWN:
        if anyEvent.key == p.K_q:
            gameFinish = False


    keys = p.key.get_pressed()
    if keys[p.K_w]:
        Paddle_a.moveUP(20)
    if keys[p.K_s]:
        Paddle_a.moveDown(20)

    keys2 = p.key.get_pressed()
    if keys2[p.K_UP]:
        Paddle_b.moveUP(20)
    if keys2[p.K_DOWN]:
        Paddle_b.moveDown(20)



    p.display.flip()

    time.tick(60)
p.quit()






























































































