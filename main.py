import pygame
from pygame. locals import *
import time
import movement

class Geek:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x
  
raj = Geek()


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PySnake')
image = pygame.image.load(r'snake_image.png')
DEFAULT_IMAGE_SIZE = (50, 50)
snake = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)



x = 400
y = 400
velocity = 50
  
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(snake, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    raj.set_age(21)
                    x -= velocity
  
                if event.key == pygame.K_RIGHT:
                    x += velocity
                    pygame.display.update()
  
                if event.key == pygame.K_UP:
                    y -= velocity
                    pygame.display.update()
  
                if event.key == pygame.K_DOWN:
                    y += velocity
                    pygame.display.update()
        
        print(raj.get_age())
        pygame.display.update()
        
    