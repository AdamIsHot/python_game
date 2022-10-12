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
positions_x = [400, 450, 500, 550]
positions_y = [400, 400, 400, 400]
number_of_points = 4

while running:
    screen.fill((255, 255, 255))




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
        horizontal_movement = True
    if direction == 2:
        x += velocity
        horizontal_movement = True
    if direction == 3:
        y -= velocity
        horizontal_movement = False
    if direction == 4:
        y += velocity
        horizontal_movement = False
    
    positions_x.append(x) # zapise do listu aktualni pozici
    positions_y.append(y)
    
    for i in range (number_of_points):
        screen.blit(snake, (positions_x[i], positions_y[i]))

    positions_x.pop(0) # smaze z listu posledni pozici
    positions_y.pop(0)

    pygame.display.update()
    pygame.time.wait(150)
        
    