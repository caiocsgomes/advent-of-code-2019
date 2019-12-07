# https://stackoverflow.com/questions/10664856/make-a-dictionary-with-duplicate-keys-in-python
from collections import defaultdict

orbits_dict = defaultdict()
with open('./day6-input.txt') as file:
    for line in file:
        planet, planet_orbiting = line.rstrip().split(')')
        orbits_dict[planet_orbiting] = planet


def count_orbits(planet_orbiting):
    if planet_orbiting == 'COM':
        return 1
    else:
        return count_orbits(orbits_dict[planet_orbiting]) + 1


counter = 0

for orbit, planet_orbiting in orbits_dict.items():
    counter += count_orbits(planet_orbiting)

print("Part1: ", counter)

santa_path = []
my_cool_path = []

santa_destination = orbits_dict['SAN']
my_destination = orbits_dict['YOU']

while True:
    if my_destination == 'COM':
        break
    else:
        my_cool_path.append(my_destination)
        my_destination = orbits_dict[my_destination]

while True:
    if santa_destination == 'COM':
        break
    else:
        santa_path.append(santa_destination)
        santa_destination = orbits_dict[santa_destination]

print("Part2: ", len(set(santa_path) ^ set(my_cool_path)))
