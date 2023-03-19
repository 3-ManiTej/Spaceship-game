import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

playerimg=pygame.image.load('house.png')
playerX=300
playerY=520

def player(x,y):
    screen.blit(playerimg,(x,y))
running=True
while running:
    for event in pygame.event.get():
        playerY-=1
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255,0,0))
    player(playerX,playerY)
    pygame.display.update()