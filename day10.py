import math

asteroids = []
with open("day10-input.txt", "r") as f:
    asteroids = [i for line in f for i in line.rstrip().split()]

def sin_cos(asteroid_from, asteroid_to):
    hypotenuse = math.sqrt((asteroid_from[0] - asteroid_to[0]) ** 2 + (asteroid_from[1] - asteroid_to[1]) ** 2)
    sin = (asteroid_from[1] - asteroid_to[1]) / hypotenuse
    cos = (asteroid_to[0] - asteroid_from[0]) / hypotenuse
    sin = math.trunc(sin * 10000) / 10000
    cos = math.trunc(cos * 10000) / 10000
    return tuple((sin, cos))


# getting tuples of asteroids coordinates
y_distance = len(asteroids)
x_distance = len(asteroids[0])
asteroids_coordinates = []
for y in range(y_distance):
    for x in range(x_distance):
        if asteroids[y][x] == '#':
            asteroids_coordinates.append((x, y))

max_seen = 0
station_position = tuple()
for asteroid_coordinate_from in asteroids_coordinates:
    asteroids_seen = set()
    for asteroids_coordinate_to in asteroids_coordinates:
        if asteroids_coordinate_to == asteroid_coordinate_from:
            continue
        asteroids_seen.add(sin_cos(asteroid_coordinate_from, asteroids_coordinate_to))
    if len(asteroids_seen) > max_seen:
        station_position = asteroid_coordinate_from
        max_seen = len(asteroids_seen)

print("Part 1:", max_seen, "asteroids seen from asteroid at position", station_position)

sin_cos_from_station = []
points_from_station = []
for asteroids_coordinate_to in asteroids_coordinates:
    if asteroids_coordinate_to == station_position:
        continue
    sin_cos_to = sin_cos(station_position, asteroids_coordinate_to)
    sin_cos_from_station.append(sin_cos_to)
    points_from_station.append(asteroids_coordinate_to)

# up: sen = 1 cos = 0 down: sen = -1 cos = 0
# right: sen = 0 cos = 1 left: sen = 0 cos = -1
first_quadrant = [i for i in sin_cos_from_station if i[0] > 0 and i[1] >= 0]
second_quadrant = [i for i in sin_cos_from_station if i[0] >= 0 and i[1] < 0]
third_quadrant = [i for i in sin_cos_from_station if i[0] < 0 and i[1] <= 0]
fourth_quadrant = [i for i in sin_cos_from_station if i[0] <= 0 and i[1] > 0]

# sort by clockwise cos sen
first_quadrant.sort(key=lambda tup: tup[1])
fourth_quadrant.sort(key=lambda tup: tup[1], reverse=True)
third_quadrant.sort(key=lambda tup: tup[1], reverse=True)
second_quadrant.sort(key=lambda tup: tup[1])

sin_cos_ordered_clockwise = first_quadrant + fourth_quadrant + third_quadrant + second_quadrant

counter = 0
last_item = ()
sin_cos_200 = ()
i = 0
turns = 0
while True:
    # if end of list is reached come back to start
    if i == (len(sin_cos_ordered_clockwise) - 1):
        i = 0
        continue

    # if items are repeated it means they are at the same angle, then jump it
    if sin_cos_ordered_clockwise[i] == last_item:
        i += 1
        continue
    else:
        if counter == 200:
            sin_cos_200 = sin_cos_ordered_clockwise[i - 1]
            break

    current = sin_cos_ordered_clockwise[i]
    # if current is in first quadrant and last in fourth it means one clockwise turn
    if last_item in fourth_quadrant and current in first_quadrant:
        turns += 1
    counter += 1
    last_item = current
    sin_cos_ordered_clockwise.pop(i)

occurrences = [i for i, val in enumerate(sin_cos_from_station) if val == sin_cos_200]
print("Part 2:", turns + 1, "nearest occurence from", station_position)
for i in occurrences:
    print(points_from_station[i])
