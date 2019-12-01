def calculateFuel(mass):
    return int(mass/3) - 2

totalFuel = 0

with open("day1-first-input.txt", "r") as line:
    for mass in line:
        totalFuel += calculateFuel(int(mass))

print(totalFuel)