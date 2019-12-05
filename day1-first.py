def calculate_fuel(mass):
    return mass//3 - 2


totalFuel = 0

with open("day1-first-input.txt", "r") as line:
    for mass in line:
        totalFuel += calculate_fuel(int(mass))

print(totalFuel)
