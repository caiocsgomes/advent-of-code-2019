import itertools
from IntcodeMachine import IntcodeMachine

software = []
with open("day9-input.txt", "r") as f:
    software = [i for line in f for i in line.rstrip().split(',')]

machine = IntcodeMachine(software[:])
machine.execute(1)
print(machine.output())
