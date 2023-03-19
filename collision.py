import math
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,600))

playerimg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change=0

enemyimg=pygame.image.load('enemy.png')
enemyX=random.randint(0,786)
enemyY=random.randint(1,45)
enemyX_change=0.3
enemyY_change=20

bulletimg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=0.3
bullet_state='ready'

score=0

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x,y))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(((enemyX-bulletX)**2)+((enemyY-bulletY)**2))
    if distance<20:
        return True
    return False

running=True

while running:
    #print(bullet_state)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                bulletX=playerX
                bullet_fire(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0


    screen.fill((100,200,0))
    playerX = playerX + playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 768:
        enemyX_change = -0.3
        enemyY += enemyY_change

    if bulletY<=0:
       bulletY=480
       bullet_state="ready" '''if we did not give this stmt bullet will repeatedly
                               be release at that location.'''

    if bullet_state=='fire':
        bullet_fire(bulletX,bulletY)
        bulletY-=bulletY_change
    player(playerX, playerY)
    enemyX = enemyX + enemyX_change
    enemy(enemyX, enemyY)

    collision=iscollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY=480
        bullet_state='ready'
        score+=1
        print(score)
        enemyX=random.randint(0,786)
        enemyY=random.randint(1,100)
    pygame.display.update()