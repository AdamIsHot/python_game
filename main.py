from difflib import SequenceMatcher
from tkinter import LEFT
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

class Geek:
    def __init__(self, x = 0, y = 0):
         self._x = x
         self._y = y
      
    # getter method
    def get_age(self):
        return self._x, self._y
      
    # setter method
    def set_age(self, X, Y):
        #sem napsat neco, aby program postupne pouzival vsechny hodnoty
        self._x = X
        self._y = Y
    
raj = Geek()

x = 400
y = 400
velocity = 50
direction = 0

t = 0
s = 0
running = True
screen.fill((255, 255, 255))
while running:
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
    
    raj.set_age(x, y)
    erase_x, erase_y = raj.get_age()

    if direction == 1:
        x -= velocity
        if t == 5:
            screen.fill((255, 255, 255), (erase_x, erase_y, 50, 50))

        else:
            t += 1
        
        
    if direction == 2:
        x += velocity
        if t == 5:
            screen.fill((255, 255, 255), (erase_x, erase_y, 50, 50))
        else:
            t += 1       
    if direction == 3:
        y -= velocity
        if t == 5:
            screen.fill((255, 255, 255), (erase_x, erase_y, 50, 50))
        else:
            t += 1
    if direction == 4:
        y += velocity
        if t == 5:
            screen.fill((255, 255, 255), (erase_x, erase_y, 50, 50))
        else:
            t += 1
    
    

    
    pygame.display.update()
    pygame.time.wait(150)
        
    