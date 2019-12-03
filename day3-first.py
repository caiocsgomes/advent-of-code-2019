import csv
import sys

moves = []
with open("day3-input.txt", "r") as file:
    reader = csv.reader(file)
    moves = list(reader)

def createPath(moves):
    coordinate = [0,0]
    coordinatesList = []
    for i in range(len(moves)):
        currentX = coordinate[0]
        currentY = coordinate[1]
        move = int(moves[i][1:])
        direction = moves[i][0]
        if direction == 'U':
            for i in range(move + 1):
                coordinatesList.append([currentX, currentY + i])
            coordinate = coordinatesList[-1]
        elif direction == 'D':
            for i in range(0, -(move + 1), -1):
                coordinatesList.append([currentX, currentY + i])
            coordinate = coordinatesList[-1]
        elif direction == 'R':
            for i in range(move + 1):
                coordinatesList.append([currentX + i, currentY])
            coordinate = coordinatesList[-1]
        elif direction == 'L':
            for i in range(0, -(move + 1), -1):
                coordinatesList.append([currentX + i, currentY])
            coordinate = coordinatesList[-1]
    return coordinatesList

def calculateDist(coordinate):
    return abs(coordinate[0]) + abs(coordinate[1])

def getSmallestDist(coordinates):
    smallestDist = sys.maxsize
    for i in range(len(coordinates)):
        distance = calculateDist(coordinates[i])
        if distance < smallestDist and distance != 0:
            smallestDist = distance
    return smallestDist

def getIntesections(coordinatesA, coordinatesB):
    intersections = []
    for i in range(len(coordinatesA)):
        for j in range(len(coordinatesB)):
            if(coordinatesA[i] == coordinatesB[j]):
                intersections.append(coordinatesA[i])
    return intersections

movementsA = createPath(moves[0])
movementsB = createPath(moves[1])

intersections = getIntesections(movementsA, movementsB)

distance = getSmallestDist(intersections)

print(distance)