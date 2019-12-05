def calculate_by_mass(mass):
    return mass//3 - 2


def calculate_total_fuel_iterative(mass):
    totalFuel = 0
    fuelByMass = calculate_by_mass(mass)
    while fuelByMass >= 1:
        totalFuel += fuelByMass
        fuelByMass = calculate_by_mass(fuelByMass)
    return totalFuel


def calculate_total_fuel_recursive(mass):
    totalFuel = calculate_by_mass(mass)
    if totalFuel >= 1:
        return (totalFuel + calculate_total_fuel_recursive(totalFuel))
    return 0


totalFuelUsingIterative = 0
totalFuelUsingRecursive = 0

with open("day1-first-input.txt", "r") as line:
    for mass in line:
        totalFuelUsingIterative += calculate_total_fuel_iterative(int(mass))
        totalFuelUsingRecursive += calculate_total_fuel_recursive(int(mass))

print("Iterative: ", totalFuelUsingIterative)
print("Recursive: ", totalFuelUsingRecursive)
