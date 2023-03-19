import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

playerimg=pygame.image.load('house.png')
playerX=300
playerY=520
X_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                X_change=-1
            if event.key==pygame.K_RIGHT:
                X_change=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                X_change=0
    playerX+=X_change
    if playerX<0:
        playerX=0
    if playerX>=768:
        playerX=768
    screen.fill((255,0,0))
    player(playerX,playerY)
    pygame.display.update()
