import pygame
from pygame. locals import *

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('PySnake')
snake = pygame.image.load(r'snake_image.png')  

x = 50
y = 50
velocity = 5
  
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(snake, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= velocity
  
                if event.key == pygame.K_RIGHT:
                    x += velocity
  
                if event.key == pygame.K_UP:
                    y -= velocity
  
                if event.key == pygame.K_DOWN:
                    y += velocity
  
        pygame.display.update()
        
    