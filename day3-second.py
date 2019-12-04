import csv
import sys

moves = []
with open("day3-input.txt", "r") as file:
    reader = csv.reader(file)
    moves = list(reader)

def createPath(moves):
    coordinate = (0, 0)
    coordinatesList = []
    for i in range(len(moves)):
        currentX = coordinate[0]
        currentY = coordinate[1]
        move = int(moves[i][1:])
        direction = moves[i][0]
        if direction == 'U':
            for i in range(move + 1):
                coordinatesList.append((currentX, currentY + i))
        elif direction == 'D':
            for i in range(0, -(move + 1), -1):
                coordinatesList.append((currentX, currentY + i))
        elif direction == 'R':
            for i in range(move + 1):
                coordinatesList.append((currentX + i, currentY))
        elif direction == 'L':
            for i in range(0, -(move + 1), -1):
                coordinatesList.append((currentX + i, currentY))
        coordinate = coordinatesList[-1]
    return coordinatesList

movementsA = createPath(moves[0])
movementsB = createPath(moves[1])

intersections = list(set(movementsA) & (set(movementsB)))

smallest = sys.maxsize
coordinate = ()
for intersection in intersections:
    distanceA = movementsA.index(intersection) - 1
    distanceB = movementsB.index(intersection) - 1
    distance = distanceA + distanceB
    if(distance < smallest and distance > 0):
        smallest = distance
        coordinate = intersection

print(smallest)