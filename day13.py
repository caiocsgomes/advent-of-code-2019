from IntcodeMachine import IntcodeMachine
from pygame.locals import *
import pygame
import sys

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

software = []
with open("day13-input.txt", "r") as f:
    software = [i for line in f for i in line.rstrip().split(',')]

machine1 = IntcodeMachine(software[:])
machine1.execute()
out1 = machine1.out()
tiles = [out1[x:x + 3] for x in range(0, len(out1), 3)]
# 0: empty 1: wall 2: block 3: horizontal paddle 4: ball
blocks = 0
for tile in tiles:
    if tile[2] == 2:
        blocks += 1

print("Part 1:", blocks)

software[0] = 2
machine = IntcodeMachine(software[:])
screen = pygame.display.set_mode((700, 600))
pygame.init()
score = 0
ball_x = 0
paddle_x = 0
inp = 0
block = 15
while not machine.halted():
    machine.execute(inp)
    out = machine.out()
    tiles = [out[x:x + 3] for x in range(0, len(out), 3)]
    for tile in tiles:
        x = tile[0]
        y = tile[1]
        element = tile[2]
        if x == -1 and y == 0:
            score = element
        # wall
        elif element == 1:
            pygame.draw.rect(screen, red, (x + x * block, y + y * block, block, block))
        # block
        elif element == 2:
            pygame.draw.rect(screen, green, (x + x * block, y + y * block, block, block))
        # horizontal paddle
        elif element == 3:
            paddle_x = x
            pygame.draw.rect(screen, blue, (x + x * block, y + y * block, block, block))
        # ball
        elif element == 4:
            ball_x = x
            pygame.draw.rect(screen, pink, (x + x * block, y + y * block, block, block))
        else:
            pygame.draw.rect(screen, black, (x + x * block, y + y * block, block, block))

    if ball_x > paddle_x:
        inp = 1
    elif paddle_x > ball_x:
        inp = -1
    else:
        inp = 0

    pygame.display.update()

print("Part 2:", score)
