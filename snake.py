import pygame
import random
import math
pygame.init()

screen=pygame.display.set_mode((800,600))

snakex=30
snakeY=30
snakex_change=0
snakey_change=0
length=50
breadth=50

foodX=random.randint(1,700)
foodY=random.randint(1,500)
food_length=50
food_breadth=50

score=0
snake_list=[]
snake=2
def fun():
    for i in range(len(snake_list)):
        pygame.draw.rect(screen, (255, 0, 0), [snake_list[i][0], snake_list[i][1], length, breadth])
    #snake_list.remove(snake_list[0])

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snakex_change+=0.1
                snakey_change=0
            if event.key==pygame.K_LEFT:
                snakex_change-=0.1
                snakey_change=0
            if event.key==pygame.K_UP:
                snakey_change-=0.1
                snakex_change=0
            if event.key==pygame.K_DOWN:
                snakey_change+=0.1
                snakex_change=0
        '''if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                snakex_change+=0.1
                snakey_change=0
            if event.key==pygame.K_LEFT:
                snakex_change-=0.1
                snakey_change=0
            if event.key == pygame.K_UP:
                snakey_change -= 0.1
                snakex_change=0
            if event.key == pygame.K_DOWN:
                snakey_change += 0.1
                snakex_change=0'''
    head=[]

    if abs(snakex-foodX)<5 and abs(snakeY-foodY)<5:
        score+=1
        print(score)
        foodX = random.randint(1, 700)
        foodY = random.randint(1, 500)
        pygame.draw.rect(screen,(255,0,0),[foodX,foodY,food_length,food_breadth])
    head.append(snakex)
    head.append(snakeY)
    snake_list.append(head)
    snakex+=snakex_change
    snakeY+=snakey_change
    screen.fill((100,0,100))
    #pygame.draw.rect(screen,(255,0,0),[snakex,snakeY,length,breadth])
    fun()

    pygame.draw.rect(screen, (0, 0, 255), [foodX, foodY, food_length, food_breadth])
    pygame.display.update()