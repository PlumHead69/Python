import pygame as p
import random
import time
from paddle import Paddle
from ball import Ball

p.init()

objectClock = p.time.Clock()

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
green = (0, 155, 0)

score_a = 0
score_b = 0
font_small = p.font.SysFont("comicsansms", 25)
font_medium = p.font.SysFont("comicsansms", 50)
font_large = p.font.SysFont("comicsansms", 80)

display_width = 800
display_height = 600

DisplayScreen = p.display.set_mode((display_width, display_height))
p.display.set_caption('PongGame')

ball = Ball()
ball.rect.x = 360
ball.rect.y = 250
ball.dx = 0.15
ball.dy = 0.15

Paddle_a = Paddle()
Paddle_a.rect.x = 50
Paddle_a.rect.y = 250

Paddle_b = Paddle()
Paddle_b.rect.x = 700
Paddle_b.rect.y = 250


paddle_list = p.sprite.Group()
paddle_list.add(Paddle_a)
paddle_list.add(Paddle_b)

Paddle_a_list = p.sprite.Group()
Paddle_a_list.add(Paddle_a)

Paddle_b_list = p.sprite.Group()
Paddle_b_list.add(Paddle_b)

ball_list = p.sprite.Group()
ball_list.add(ball)


def choose_game():
    intro_screen = True
    
    while intro_screen:

        for eachEvent in p.event.get():
            if eachEvent.type == p.QUIT:
                p.quit()
                quit()

            if eachEvent.type == p.KEYDOWN:
                if eachEvent.key == p.K_c:
                    intro_screen = False
                    return False
                    
                if eachEvent.key == p.K_v:
                    intro_screen = False
                    return True
                    
                if eachEvent.key == p.K_q:
                    p.quit()
                    quit()

        DisplayScreen.fill(color_black)
        display_ScreenMessage("Welcome to Pong",
                              color_white,
                              -100,
                              "large")
        display_ScreenMessage("",
                              color_black,
                              -30)

        display_ScreenMessage("",
                              color_black,
                              10)

        display_ScreenMessage("Made by FERÓÓÓÓÓ",
                              color_red,
                              50)

        display_ScreenMessage("Press C to play multi or V to play single.",
                              color_white,
                              100)
        display_ScreenMessage("",
                              color_black,
                              10)
        display_ScreenMessage("Q to quit.",
                              color_white,
                              180,
                              "small")

        p.display.update()


def objects_text(sample_text, sample_color, sample_size):
    if sample_size == "small":
        surface_for_text = font_small.render(sample_text, True, sample_color)
    elif sample_size == "medium":
        surface_for_text = font_medium.render(sample_text, True, sample_color)
    elif sample_size == "large":
        surface_for_text = font_large.render(sample_text, True, sample_color)

    return surface_for_text, surface_for_text.get_rect()


def display_ScreenMessage(message, font_color, yDisplace=0, font_size="small"):
    textSurface, textRectShape = objects_text(message, font_color, font_size)
    textRectShape.center = (
        display_width / 2), (display_height / 2) + yDisplace
    DisplayScreen.blit(textSurface, textRectShape)


def move_ball():
    ball.setx(80)
    ball.sety(80)


def main(gametype):
    movex = 5
    movey = 5
    score_a = 0
    score_b = 0
    gameFinish = True
    singlePlayer=gametype
    while gameFinish == True:
        bBounce=1
        for anyEvent in p.event.get():
            if anyEvent.type == p.QUIT:
                gameFinish = False
        
        if score_a == 10 or score_b == 10:
            gameFinish=False
        DisplayScreen.fill(color_black)
        display_ScreenMessage("Player A: {}  Player B: {}".format(score_a, score_b), color_white)
        

        ball.setx(movex)
        ball.sety(movey)

        if ball.rect.y > 590 or ball.rect.y < 10:
            movey *= -bBounce

        hit_collision = p.sprite.spritecollide(
            ball, Paddle_a_list, False, p.sprite.collide_mask)
        for bounce in hit_collision:
            ball.rect.x=90
            movex *= -bBounce

        hit_collision2 = p.sprite.spritecollide(
            ball, Paddle_b_list, False, p.sprite.collide_mask)
        for bounce in hit_collision2:
            ball.rect.x=660
            movex *= -bBounce

        if ball.rect.x > 760:
            ball.rect.x = 360
            ball.rect.y = 250 *random.random()
            movex *= -bBounce
            score_a += 1
            

        if ball.rect.x < 15:
            ball.rect.x = 360
            ball.rect.y = 250 *random.random()
            movex *= -1
            score_b += 1
            

        keys = p.key.get_pressed()
        if keys[p.K_w]:
            Paddle_a.moveUP(10)
        if keys[p.K_s]:
            Paddle_a.moveDown(10)


        if singlePlayer==True:
            if ball.rect.y+5 > Paddle_b.rect.y:
                Paddle_b.moveDown(10)
            if ball.rect.y-5 < Paddle_b.rect.y:
                Paddle_b.moveUP(10)
        else:
            keys2 = p.key.get_pressed()
            if keys2[p.K_UP]:
                Paddle_b.moveUP(10)
            if keys2[p.K_DOWN]:
                Paddle_b.moveDown(10)




        paddle_list.draw(DisplayScreen)
        ball_list.draw(DisplayScreen)
        p.display.flip()
        objectClock.tick(60)
    p.quit()



main(choose_game())
































































































