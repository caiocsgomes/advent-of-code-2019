numbers = []

with open("day2-first-input.txt", "r") as file:
    for line in file:
        textLine = line.rstrip("\n")
        numbers = list(map(int, textLine.split(",")))

numbers[1] = 12
numbers[2] = 2

for i in range(0, len(numbers), 4):
    if numbers[i] == 1 :
        numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers [numbers[i + 2]]
    elif numbers[i] == 2:
        numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers [numbers[i + 2]]
    elif numbers[i] == 99:
        break

print(numbers[0])