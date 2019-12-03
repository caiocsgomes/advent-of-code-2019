import csv, sys

with open("day3-input.txt", "r") as file:
    reader = csv.reader(file)
    moves = list(reader)

U = 0 + 1j
D = 0 - 1j
L = -1 + 0j
R = 1 + 0j

