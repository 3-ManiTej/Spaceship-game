import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))

playerimg=pygame.image.load('house.png')
playerX=360
playerY=520

#blit is used to draw the image in window
def player():
    screen.blit(playerimg,(playerX,playerY))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((0,200,0))
    player()
    pygame.display.update()