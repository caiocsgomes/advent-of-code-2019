import re

coordinates = []
with open("day12-input.txt", "r") as f:
    coordinates = [i for line in f for i in re.sub('[<>=xyz]', '', line).rstrip().split(',')]


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __eq__(self, other):
        return (self.x == other.x) \
            and (self.y == other.y) \
            and (self.z == other.z) \
            and (self.vx == other.vx) \
            and (self.vy == other.vy) \
            and (self.vz == other.vz)

moons = []
for i in range(0, len(coordinates), 3):
    x, y, z = map(int, coordinates[i: i + 3])
    moons.append(Moon(x, y, z))

for _ in range(1000):
    for moon_from in moons:
        for moon_to in moons:
            if moon_from == moon_to:
                continue

            if moon_from.x > moon_to.x:
                moon_from.vx -= 1
            elif moon_from.x < moon_to.x:
                moon_from.vx += 1

            if moon_from.y > moon_to.y:
                moon_from.vy -= 1
            elif moon_from.y < moon_to.y:
                moon_from.vy += 1

            if moon_from.z > moon_to.z:
                moon_from.vz -= 1
            elif moon_from.z < moon_to.z:
                moon_from.vz += 1

    for moon in moons:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz

kinetic_energy = 0
for moon in moons:
    kinetic_energy += (sum([abs(moon.x), abs(moon.y), abs(moon.z)]) * sum([abs(moon.vx), abs(moon.vy), abs(moon.vz)]))

print("Part 1:", kinetic_energy)


moons = []
for i in range(0, len(coordinates), 3):
    x, y, z = map(int, coordinates[i: i + 3])
    moons.append(Moon(x, y, z))

moons_copy = []
for i in range(0, len(coordinates), 3):
    x, y, z = map(int, coordinates[i: i + 3])
    moons_copy.append(Moon(x, y, z))

steps = 0

while True:
    for moon_from in moons:
        for moon_to in moons:
            if moon_from == moon_to:
                continue

            if moon_from.x > moon_to.x:
                moon_from.vx -= 1
            elif moon_from.x < moon_to.x:
                moon_from.vx += 1

            if moon_from.y > moon_to.y:
                moon_from.vy -= 1
            elif moon_from.y < moon_to.y:
                moon_from.vy += 1

            if moon_from.z > moon_to.z:
                moon_from.vz -= 1
            elif moon_from.z < moon_to.z:
                moon_from.vz += 1

    for moon in moons:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz

    steps += 1

    if moons[0] == moons_copy[0] \
            and moons[1] == moons_copy[1] \
            and moons[2] == moons_copy[2]:
        break

print(steps)