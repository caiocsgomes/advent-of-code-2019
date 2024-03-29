import csv
import sys

moves = []
with open("day3-input.txt", "r") as file:
    reader = csv.reader(file)
    moves = list(reader)


def create_path(moves):
    coordinate = (0, 0)
    coordinatesList = []
    for i in range(len(moves)):
        currentX = coordinate[0]
        currentY = coordinate[1]
        move = int(moves[i][1:])
        direction = moves[i][0]
        if direction == 'U':
            for i in range(1, move + 1, 1):
                coordinatesList.append((currentX, currentY + i))
        elif direction == 'D':
            for i in range(-1, -(move + 1), -1):
                coordinatesList.append((currentX, currentY + i))
        elif direction == 'R':
            for i in range(1, move + 1, 1):
                coordinatesList.append((currentX + i, currentY))
        elif direction == 'L':
            for i in range(-1, -(move + 1), -1):
                coordinatesList.append((currentX + i, currentY))
        coordinate = coordinatesList[-1]
    return coordinatesList


movementsA = create_path(moves[0])
movementsB = create_path(moves[1])

intersections = list(set(movementsA) & (set(movementsB)))

smallest = sys.maxsize
for intersection in intersections:
    distance = movementsA.index(intersection) + movementsB.index(intersection) + 2
    if (distance < smallest and distance > 0):
        smallest = distance

print(smallest)
