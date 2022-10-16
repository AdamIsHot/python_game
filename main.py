import pygame
import movement as m

pygame.init()

# screen essentials
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PySnake')

# images essentials
image = pygame.image.load(r'snake_image.png')
image2 = pygame.image.load(r'jablko.png')
DEFAULT_IMAGE_SIZE = (50, 50)
snake = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
apple = pygame.transform.scale(image2, DEFAULT_IMAGE_SIZE)

# text essetials
red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 64)
text = font.render('Lost', True, red)
textRect = text.get_rect()
textRect.center = (400, 400)

# movement essentials
velocity = 50
direction = 0
horizontal_movement = False

# positions essentials
x = 400
y = 400
positions_x = [550, 500, 450, 400]
positions_y = [400, 400, 400, 400]
apple_positons = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750]
apple_x, apple_y = m.next_apple(apple_positons, len(positions_x), positions_x, positions_y)

# game running essentials
game_started = False
ended_move = False
lost = False

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not horizontal_movement and not ended_move:
                direction = 1; horizontal_movement = True; game_started = True; ended_move = True
            if event.key == pygame.K_d and not horizontal_movement and game_started and not ended_move:
                direction = 2; horizontal_movement = True; ended_move = True
            if event.key == pygame.K_w and not ended_move:
                if not game_started:
                    direction = 3; horizontal_movement = False; game_started = True; ended_move = True
                elif horizontal_movement:
                    direction = 3; horizontal_movement = False; game_started = True; ended_move = True
                    
            if event.key == pygame.K_s and not ended_move:
                if not game_started:
                    direction = 4; horizontal_movement = False; game_started = True; ended_move = True
                elif horizontal_movement:
                    direction = 4; horizontal_movement = False; game_started = True; ended_move = True
                    
                
    if game_started:
        
        if not lost:
            x, y = m.next_direction(x, y, direction, velocity)
            positions_x.append(x) # zapise do listu aktualni pozici
            positions_y.append(y)
        
        if m.lose(len(positions_x), x, y, positions_x, positions_y, game_started):
            lost = True
            screen.blit(text, textRect)
            positions_x.pop(len(positions_x) - 1)
            positions_y.pop(len(positions_y) - 1)
        else:
            if x == apple_x and y == apple_y:
                apple_x, apple_y = m.next_apple(apple_positons, len(positions_x), positions_x, positions_y)
            else:
                positions_x.pop(0) # smaze z listu posledni pozici
                positions_y.pop(0)



    for i in range (len(positions_x)):
        screen.blit(snake, (positions_x[i], positions_y[i]))
        
    screen.blit(apple, (apple_x, apple_y))
    pygame.display.update()
    ended_move = False
    if lost:
        pygame.time.wait(1500)
        running = False
    else:
        pygame.time.wait(130)