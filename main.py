import pygame
from pygame. locals import *
import time
import movement

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PySnake')
image = pygame.image.load(r'snake_image.png')
DEFAULT_IMAGE_SIZE = (50, 50)
snake = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)


x = 400
y = 400
velocity = 50
direction = 0

  
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(snake, (x, y))

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = 1
  
                if event.key == pygame.K_d:
                    direction = 2

                if event.key == pygame.K_w:
                    direction = 3
  
                if event.key == pygame.K_s:
                    direction = 4
    

    if direction == 1:
        x -= velocity
    if direction == 2:
        x += velocity
    if direction == 3:
        y -= velocity
    if direction == 4:
        y += velocity

    screen.fill((255, 255, 255))
    screen.blit(snake, (x, y))
    
    pygame.display.update()
    pygame.time.wait(150)
        
    