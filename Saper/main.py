import pygame
import random

screen_width = 600
screen_height = 600
width = 25
height = 25
bombs = 75
border = 1
clicked = False


field = []
for x in range(screen_width//width):
    field.append([])
    for y in range(screen_height//height):
        field[x].append((0, True))



      


pygame.init()
font = pygame.font.SysFont("Arial", int(height*0.8))
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = (event.pos[0]//width, event.pos[1]//height)
            cell = field[pos[0]][pos[1]]
            if cell[1]:
                if cell[0] == -1:
                    running = False
                else:
                    field[pos[0]][pos[1]] = (cell[0], False)
            if not clicked:
                for i in range(bombs):
                    while True:
                        x = random.randrange(screen_width // width)
                        y = random.randrange(screen_height // height)
                        if field[x][y][0] != -1 and pos[0] != x and pos[1] != y:
                            field[x][y] = (-1, True)
                            for i in range(x-1, x+2):
                                for j in range(y-1, y+2):
                                    if 0 <= i < screen_width // width and 0 <= j < screen_height // height:
                                        if field[i][j][0] != -1:
                                            field[i][j] = (field[i][j][0] + 1, field[i][j][1])
                            break
                clicked = True
            if field[pos[0]][pos[1]][0] == 0:
                empt = [pos]
                k = 0
                while k < len(empt):
                    a = empt[k]
                    for i in range(a[0]-1, a[0]+2):
                        for j in range(a[1]-1, a[1]+2):
                            if 0 <= i < screen_width // width and 0 <= j < screen_height // height:
                                if a != (i, j) and field[i][j][1]:
                                    if field[i][j][0] == 0:
                                        empt.append((i, j))
                                    field[i][j] = (field[i][j][0], False)
                    k = k + 1
    screen.fill ((0, 0, 0))
    for x in range(len(field)):
        for y in range(len(field[x])):
            cell = (x*width+border, y*height+border, width-2*border, height-2*border)
            if field[x][y][1]:
                screen.fill((255, 255, 255), cell)
            else:
                if field[x][y][0] == -1:
                    screen.fill((120, 81, 169), cell)
                elif field[x][y][0] == 0:
                    screen.fill((0, 130, 0), cell)
                else:
                    screen.fill((245, 245, 50), cell)
                    text = font.render(str(field[x][y][0]), True, (230, 0, 0))
                    screen.blit(text, (x*width, y*height))
    pygame.display.flip()