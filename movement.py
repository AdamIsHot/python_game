import pygame
import random

def next_direction(x, y, direction, velocity):
    if direction == 1:
        x -= velocity
    if direction == 2:
        x += velocity
    if direction == 3:
        y -= velocity
    if direction == 4:
        y += velocity
    return x, y

def next_apple(apple_positons, number_of_points, positions_x, positions_y):
    apple_on_snake = True
    while apple_on_snake:
        apple_x = random.choice(apple_positons)
        apple_y = random.choice(apple_positons)
        apple_on_snake = False
        for n in range(number_of_points):
            if apple_x == positions_x[n] and apple_y == positions_y[n]:
                apple_on_snake = True

    return apple_x, apple_y

def lose(number_of_points, x, y, positions_x, positions_y):
    for p in range (number_of_points - 1): # zde poznava zda nenarazil sam na sebe
        if x == positions_x[p] and y == positions_y[p] or x < 0 or x > 750 or y < 0 or y > 750:
            return True
    return False

def control(direction, event):
    if event.key == pygame.K_a and direction != 2:
        return 1, True
    if event.key == pygame.K_d and direction != 1:
        return 2, True
    if event.key == pygame.K_w and direction != 4:
        return 3, True
    if event.key == pygame.K_s and direction != 3:
        return 4, True
    return direction, True

    