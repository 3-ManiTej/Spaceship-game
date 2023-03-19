import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

playerimg=pygame.image.load('house.png')
playerX=300
playerY=520
playerX_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            #print('BUTTON IS PRESSED')
            if event.key==pygame.K_LEFT:
                #print('LEFT BUTTON IS PRESSED')
                playerX_change=-0.1
            if event.key==pygame.K_RIGHT:
                #print('RIGHT BUTTON IS PRESSED')
                playerX_change=0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("BUTTON IS RELEASED")
                playerX_change=0
    playerX+=playerX_change
    screen.fill((255,0,0))
    player(playerX,playerY)
    pygame.display.update()