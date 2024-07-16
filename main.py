import pygame
import movement as m
import body_directions as bd

pygame.init()

# screen variables
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PySnake')

# images variables
image = pygame.image.load(r'snake_image.png')
image2 = pygame.image.load(r'jablko.png')
image3 = pygame.image.load(r'ecstasy.png')
image4 = pygame.image.load(r'head_snake.png')
image5 = pygame.image.load(r'body_straight_snake.png')
image6 = pygame.image.load(r'body_to_left_snake.png')
image7 = pygame.image.load(r'body_to_right_snake.png')
image8 = pygame.image.load(r'tail_snake.png')
DEFAULT_IMAGE_SIZE = (50, 50)
snake = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
apple = pygame.transform.scale(image2, DEFAULT_IMAGE_SIZE)
emko = pygame.transform.scale(image3, DEFAULT_IMAGE_SIZE)
head = pygame.transform.scale(image4,  DEFAULT_IMAGE_SIZE)
straight_body = pygame.transform.scale(image5, DEFAULT_IMAGE_SIZE)
left_body = pygame.transform.scale(image6, DEFAULT_IMAGE_SIZE)
right_body = pygame.transform.scale(image7, DEFAULT_IMAGE_SIZE)
tail = pygame.transform.scale(image8, DEFAULT_IMAGE_SIZE)

# text variables
red = (255, 0, 0)
blue = (51, 102, 153)
yellow = (0, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 64)
font2 = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Lost', True, red)
textRect = text.get_rect()
textRect.center = (400, 400)
textRect2 = text.get_rect()
textRect2.center = (70, 40)
textRect3 = text.get_rect()
textRect3.center = (150, 40)

# movement variables
velocity = 50
direction = 1
horizontal_movement = 2

# positions variables
x = 400
y = 400
positions_x = [550, 500, 450, 400]
positions_y = [400, 400, 400, 400]
last_position_x = 600
last_position_y = 400
apple_positons = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750]
apple_x, apple_y = m.next_apple(apple_positons, len(positions_x), positions_x, positions_y)
emo_x, emo_y = m.next_apple(apple_positons, len(positions_x), positions_x, positions_y)

# game running variables
game_started = False
ended_move = False
lost = False
wait_time = 135
highest_score = m.HighestScore()
score = 0

# game runner
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not ended_move:
            direction, ended_move = m.control(direction, event)
            game_started = True
    
    if game_started:
        if not lost:
            x, y = m.next_direction(x, y, direction, velocity)
            positions_x.append(x) # zapise do listu aktualni pozici
            positions_y.append(y)
        
        if m.lose(len(positions_x), x, y, positions_x, positions_y):
            lost = True
            positions_x.pop(len(positions_x) - 1)
            positions_y.pop(len(positions_y) - 1)
        else:
            if x == apple_x and y == apple_y:
                score += 1
                apple_x, apple_y = m.next_apple(apple_positons, len(positions_x), positions_x, positions_y)
            else:
                last_position_x = positions_x[0]
                last_position_y = positions_y[0]
                positions_x.pop(0) # smaze z listu posledni pozici
                positions_y.pop(0)

            if x == emo_x and y == emo_y:
                emo_x, emo_y = m.next_apple(apple_positons, len(positions_x), positions_x, positions_y)
                wait_time -= 10
    
    # rendering head
    angle_head = pygame.transform.rotate(head, bd.head_direction(positions_x, positions_y))
    screen.blit(angle_head, (positions_x[len(positions_x)-1], positions_y[len(positions_y)-1]))

    # rendering tail
    angle_tail = pygame.transform.rotate(tail, bd.tail_direction(positions_x, positions_y, last_position_x, last_position_y))
    screen.blit(angle_tail, (positions_x[0], positions_y[0]))

    # rendering body
    for i in range (1, len(positions_x)-1):
        
        screen.blit(snake, (positions_x[i], positions_y[i]))

    screen.blit(apple, (apple_x, apple_y))
    screen.blit(emko, (emo_x, emo_y))

    f = open("highest_score.txt", "r")
    highest_score.set_highest_score(int(f.read(1)))
    f.close()
    
    if highest_score.get_highest_score() < score:
        f = open("highest_score.txt", "w")
        f.write(str(score))
        f.close()
    
    text2 = font2.render('Score: ' + str(score), True, blue)
    text3 = font2.render('Highest score: ' + str(highest_score.get_highest_score()), True, yellow)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)

    if lost:
        screen.blit(text, textRect)

    pygame.display.update()
    ended_move = False
    if lost:
        pygame.time.wait(1500)
        running = False
    else:
        pygame.time.wait(wait_time)