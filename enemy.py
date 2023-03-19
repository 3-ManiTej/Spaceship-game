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

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x,y))


running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            '''if event.key == pygame.K_SPACE:
                bulletX=playerX
                bullet_fire(bulletX,bulletY)'''
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

    bullet_fire(playerX,bulletY)
    bulletX = playerX
    #if bullet_state=='fire':
    bullet_fire(bulletX,bulletY)
    bulletY-=bulletY_change
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'
    bullet_fire(bulletX,bulletY)
    player(playerX, playerY)
    enemyX = enemyX + enemyX_change
    enemy(enemyX, enemyY)

    pygame.display.update()