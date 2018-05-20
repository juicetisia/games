import pygame
import random

def spawn_food():
    while True:
        x = random.randrange(screen_width // width)
        y = random.randrange(screen_height // height)
        if (x, y) not in snake:
            return (x, y)

screen_width = 800
screen_height = 600
width = 25
height = 25
default_size = 3
direction = (1, 0)
dir_changed = False
snake = []
for i in reversed(range(default_size)):
    x = screen_width // 2 // width - i
    y = screen_height // 2 // height
    snake.append((x, y))


food = spawn_food()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
update_timer = pygame.USEREVENT + 1
pygame.time.set_timer(update_timer, 300)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == update_timer:
            head = ((snake[-1][0] + direction[0]) % (screen_width // width), (snake[-1][1] + direction[1]) % (screen_height // height))
            if head in snake:
                running = False
            snake.append(head)
            if snake[-1] == food:
                food = spawn_food()
            else:
                del snake[0]
            dir_changed = False
        elif event.type == pygame.KEYDOWN:
            if not dir_changed:
                if event.key == pygame.K_UP and direction[0] != 0:
                    direction = (0, -1)
                    dir_changed = True
                elif event.key == pygame.K_DOWN and direction[0] != 0:
                    direction = (0, 1)  
                    dir_changed = True  
                elif event.key == pygame.K_LEFT and direction[1] != 0:
                    direction = (-1, 0)
                    dir_changed = True
                elif event.key == pygame.K_RIGHT and direction[1] != 0:
                    direction = (1, 0)   
                    dir_changed = True         
    screen.fill((0, 100, 0))
    for x, y in snake:
        screen.fill((134, 100, 100), (width*x, height*y, width, height))
    screen.fill((230, 0, 0), (food[0]*width, food[1]*height, width, height))
    pygame.display.flip()



