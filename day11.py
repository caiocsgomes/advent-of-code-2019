from IntcodeMachine import IntcodeMachine

software = []
with open("day11-input.txt", "r") as f:
    software = [i for line in f for i in line.rstrip().split(',')]


# 0: black 1: white
# 0: left 90 degrees 1: right 90 degrees

def turn_direction(face, inp):
    if face == 'up':
        if inp == 0:
            return 'left', (-1, 0)
        else:
            return 'right', (1, 0)
    elif face == 'down':
        if inp == 0:
            return 'right', (1, 0)
        else:
            return 'left', (-1, 0)
    elif face == 'left':
        if inp == 0:
            return 'down', (0, -1)
        else:
            return 'up', (0, 1)
    else:
        if inp == 0:
            return 'up', (0, 1)
        else:
            return 'down', (0, -1)


curr_face = 'up'
curr_pos = (0, 0)
canvas = 10 * [10 * [0]]
machine = IntcodeMachine(software[:])
steps = 0

# first output: color to paint
# second: direction
while machine is not machine.halted():
    machine.execute(canvas[curr_pos[0]][curr_pos[1]])
    out = machine.out()
    curr_face, mov = turn_direction(curr_face, out[1])
    canvas[curr_pos[0]][curr_pos[1]] = out[0]
    curr_pos = (curr_pos[0] + mov[0], curr_pos[1] + mov[1])
    steps += 1

print(steps)