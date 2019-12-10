import math

asteroids = []
with open("day10-input.txt", "r") as f:
    asteroids = [i for line in f for i in line.rstrip().split()]


def sen_cos(asteroid_from, asteroid_to):
    hypotenuse = math.sqrt((asteroid_from[0] - asteroid_to[0]) ** 2 + (asteroid_from[1] - asteroid_to[1]) ** 2)
    if hypotenuse == 0:
        return asteroid_from
    sen = (asteroid_to[0] - asteroid_from[0]) / hypotenuse
    cos = (asteroid_to[1] - asteroid_from[1]) / hypotenuse
    sen = math.trunc(sen * 10000) / 10000
    cos = math.trunc(cos * 10000) / 10000
    return tuple((sen, cos))


# getting tuples of asteroids coordinates
y_distance = len(asteroids)
x_distance = len(asteroids[0])
asteroids_coordinates = []
for x in range(x_distance):
    for y in range(y_distance):
        if asteroids[x][y] == '#':
            asteroids_coordinates.append((x, y))

max_seen = 0
for asteroid_coordinate_from in asteroids_coordinates:
    asteroids_seen = set()
    for asteroids_coordinate_to in asteroids_coordinates:
        asteroids_seen.add(sen_cos(asteroid_coordinate_from, asteroids_coordinate_to))
    if len(asteroids_seen) > max_seen:
        max_seen = len(asteroids_seen)

print("Part 1:", max_seen - 1)
