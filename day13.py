from IntcodeMachine import IntcodeMachine
import pygame
import random

software = []
with open("day13-input.txt", "r") as f:
    software = [i for line in f for i in line.rstrip().split(',')]

machine = IntcodeMachine(software[:])
machine.execute()
out1 = machine.out()
tiles = [out1[x:x + 3] for x in range(0, len(out1), 3)]
# 0: empty 1: wall 2: block 3: horizontal paddle 4: ball
blocks = 0
for tile in tiles:
    if tile[2] == 2:
        blocks += 1

print("Part 1:", blocks)

software[0] = 2
machine.reset_software(software[:])

pygame.init()
screen = pygame.display.set_mode((300, 400))
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
score = 0
paddle_position = tuple()
inp = 0
width = 50
height = 50
run = True
while run:
    pygame.time.delay(1000)
    machine.execute(inp)
    out2 = machine.out()
    tiles = [out1[x:x + 3] for x in range(0, len(out1), 3)]
    for tile in tiles:
        x = tile[0]
        y = tile[1]
        element = tile[2]
        if x == -1 and y == 0:
            score = element
        # empty
        elif element == 0:
            pygame.draw.rect(screen, black, (x, y, width, height))
        # wall
        elif element == 1:
            pygame.draw.rect(screen, red, (x, y, width, height))
        # block
        elif element == 2:
            pygame.draw.rect(screen, green, (x, y, width, height))
        # horizontal paddle
        elif element == 3:
            pygame.draw.rect(screen, blue, (x, y, width, height))
        # ball
        elif element == 4:
            pygame.draw.rect(screen, pink, (x, y, width, height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        inp = 1
        break
    elif keys[pygame.K_LEFT]:
        inp = -1
        break
    elif keys[pygame.K_DOWN]:
        inp = 0
        break
    pygame.display.update()
    # if machine.halted():
    #     break
print("Part 2:", score)
