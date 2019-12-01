def calculateFuelByMass(mass):
    return int(mass / 3) - 2

def calculateFuelByModuleIterative(mass):
    totalFuel = 0
    fuelByMass = calculateFuelByMass(mass)
    while fuelByMass >= 1:
        totalFuel += fuelByMass
        fuelByMass = calculateFuelByMass(fuelByMass)
    return totalFuel

def calculateFuelByModuleRecursive(mass):
    totalFuel = calculateFuelByMass(mass)
    if totalFuel >= 1:
        return (totalFuel + calculateFuelByModuleRecursive(totalFuel))
    return 0

totalFuelUsingIterative = 0
totalFuelUsingRecursive = 0

with open("day1-first-input.txt", "r") as line:
    for mass in line:
        totalFuelUsingIterative += calculateFuelByModuleIterative(int(mass))
        totalFuelUsingRecursive += calculateFuelByModuleRecursive(int(mass))

print(totalFuelUsingIterative)
print(totalFuelUsingRecursive)