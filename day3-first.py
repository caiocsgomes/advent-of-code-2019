import csv

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
        if(moves[i][0] == 'U'):
            coordinatesList.append([currentX, currentY + move])
        if(moves[i][0] == 'D'):
            coordinatesList.append([currentX, currentY - move])
        if(moves[i][0] == 'R'):
            coordinatesList.append([currentX + move, currentY])
        if(moves[i][0] == 'L'):
            coordinatesList.append([currentX - move, currentY])
        coordinate = coordinatesList[-1][:]
    return coordinatesList

def calculateDist(coordinate):
    return abs(int(moves[0][1:])) + abs(int(moves[1][1:]))

movementsA = createPath(moves[0])
movementsB = createPath(moves[1])

intersections = []

for i in range(len(movementsA)):
    for j in range(len(movementsB)):
        pointA = movementsA[i]
        pointB = movementsB[j]
        if(pointA[0] == pointB[0] and pointA[1] == pointB[1]):
            intersections.append(movementsA[i])

print(intersections)

