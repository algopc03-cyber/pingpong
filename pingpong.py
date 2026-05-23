from pygame import *
from random import randint
from time import time as timer
win_width = 700
win_height = 500
display.set_caption('PingPong')
window = display.set_mode((win_width,win_height))
window.fill((0,255,255))

player = 'palki.png'
ball = 'thumbnail_1.png'

font.init()
font1 = font.SysFont('Arial',35)
font2 = font.SysFont('Arial', 35)
lose1 = font1.render('PLAYER 1 LOSE',True,(180,0,0))
lose2 = font1.render('PLAYER 2 LOSE', True,(180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
player_1 = Player(player,10,win_height/2,20,140,10 )
player_2 = Player(player,win_width-30 ,win_height/2,20,140,10 )
ball_1 = GameSprite(ball,win_width/2, win_height/2,50,50,10)

x_speed = 15
y_speed = 15

run = True

while run:
    window.fill((0,255,255))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if run != False:
        ball_1.rect.x+=x_speed
        ball_1.rect.y+=y_speed
    if ball_1.rect.y > win_height-50 or ball_1.rect.y < 0:
        y_speed *= -1
    if sprite.collide_rect(player_1,ball_1) or sprite.collide_rect(player_2, ball_1):
        x_speed*= -1
    if ball_1.rect.x <0:
        window.blit(lose1,(250,200))

    if ball_1.rect.x > 650:
        window.blit(lose2,(250,200))

        
    ball_1.reset()
    player_1.reset()
    player_1.update1()
    player_2.reset()
    player_2.update2()
    display.update()
    time.delay(50)
