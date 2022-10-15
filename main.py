from difflib import SequenceMatcher
from tkinter import LEFT
import pygame
from pygame. locals import *
import movement as m
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PySnake')
image = pygame.image.load(r'snake_image.png')
image2 = pygame.image.load(r'jablko.png')
DEFAULT_IMAGE_SIZE = (50, 50)
snake = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
apple = pygame.transform.scale(image2, DEFAULT_IMAGE_SIZE)

red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Lose', True, red)
textRect = text.get_rect()
textRect.center = (400 // 2, 400 // 2)

velocity = 50
direction = 0

t = 0
s = 0
running = True
positions_x = [550, 500, 450, 400]
positions_y = [400, 400, 400, 400]
number_of_points = 4
horizontal_movement = False
apple_positons = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750]
apple_x = random.choice(apple_positons)
apple_y = random.choice(apple_positons)
x = 400
y = 400
game_started = False

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not horizontal_movement:
                direction = 1; horizontal_movement = True; game_started = True
            if event.key == pygame.K_d and not horizontal_movement and game_started:
                direction = 2; horizontal_movement = True
            if event.key == pygame.K_w:
                if not game_started:
                    direction = 3; horizontal_movement = False; game_started = True
                elif horizontal_movement:
                    direction = 3; horizontal_movement = False; game_started = True
            if event.key == pygame.K_s:
                if not game_started:
                    direction = 4; horizontal_movement = False; game_started = True
                elif horizontal_movement:
                    direction = 4; horizontal_movement = False; game_started = True
                    
                
    if game_started:
        x, y = m.next_direction(x, y, direction, velocity)
        positions_x.append(x) # zapise do listu aktualni pozici
        positions_y.append(y)

        if x == apple_x and y == apple_y:
            apple_x, apple_y = m.next_apple(apple_positons, number_of_points, positions_x, positions_y)
            number_of_points += 1
        else:
            positions_x.pop(0) # smaze z listu posledni pozici
            positions_y.pop(0)

        if m.lose(number_of_points, x, y, positions_x, positions_y, game_started):
            screen.blit(text, textRect)   


    for i in range (number_of_points):
        screen.blit(snake, (positions_x[i], positions_y[i]))
        
    

    

    screen.blit(apple, (apple_x, apple_y))
    
    pygame.display.update()
    pygame.time.wait(130)