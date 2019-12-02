numbers = []

with open("day2-first-input.txt", "r") as file:
    for line in file:
        textLine = line.rstrip("\n")
        numbers = list(map(int, textLine.split(",")))

numbers[1] = 12
numbers[2] = 2

for i in range(0, len(numbers), 4):
    operation = numbers[i]
    firstArgument = numbers[i + 1]
    secondArgument = numbers[i + 2]
    outputIndex = numbers[i + 3]
    if  operation == 1 :
        numbers[outputIndex] = numbers[firstArgument] + numbers[secondArgument]
    elif operation == 2:
        numbers[outputIndex] = numbers[firstArgument] * numbers[secondArgument]
    elif operation == 99:
        break

print(numbers[0])