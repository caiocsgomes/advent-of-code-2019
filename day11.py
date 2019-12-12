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


def draw_canvas(canvas, soft):
    curr_face = 'up'
    width = len(canvas[0])
    height = len(canvas)
    curr_pos = (width // 2, height // 2)
    machine = IntcodeMachine(soft[:])
    panels_painted = set()
    # first output: color to paint
    # second: direction
    while machine is not machine.halted():
        inp = canvas[curr_pos[0]][curr_pos[1]]
        machine.execute(inp)
        out = machine.out()
        if len(out) == 0:  # the machine has no output
            break
        curr_face, mov = turn_direction(curr_face, out[1])
        canvas[curr_pos[0]][curr_pos[1]] = out[0]
        curr_pos = (curr_pos[0] + mov[0], curr_pos[1] + mov[1])
        panels_painted.add(curr_pos)

    white_color = bytes((219,)).decode('cp437')

    for x in range(width):
        for y in range(height):
            if canvas[x][y] == 0:
                canvas[x][y] = ''
            else:
                canvas[x][y] = white_color

    return canvas, len(panels_painted)


canvas = [[0] * 100 for _ in range(100)]
_, panels_painted = draw_canvas(canvas, software)
print("Part 1:", panels_painted)

canvas = [[0] * 100 for _ in range(100)]
canvas[50][50] = 1

registration_canvas, _ = draw_canvas(canvas, software)

print("Part 2:")
for panel in registration_canvas:
    print(' '.join(panel))
