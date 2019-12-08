import itertools
from IntcodeMachine import IntcodeMachine

software = []
with open("day7-input.txt", "r") as f:
    software = [i for line in f for i in line.rstrip().split(',')]

perms = list(itertools.permutations(range(5, 10)))
results = []
for perm in perms:
    machines = [IntcodeMachine(software[:]) for i in range(5)]
    current = 0
    last = 4
    while not machines[current].halted():
        if not machines[current].started():
            machines[current].execute(perm[current])
        else:
            machines[current].execute(machines[last].output())
        if current == 4:
            current = 0
            last = 4
        else:
            last = current
            current += 1

    results.append(machines[4].output())

print("Part2 :", max(results))
