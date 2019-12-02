numbers= []
with open("day2-first-input.txt", "r") as file:
    for line in file:
        textLine = line.rstrip("\n")
        numbers = list(map(int, textLine.split(",")))

def calculateOutput(numbers, firstInput, secondInput):
    numbers[1] = firstInput
    numbers[2] = secondInput
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
    return numbers[0]

ans = 0
for noun in range(100):
    for verb in range(100):
        if(calculateOutput(numbers[:], noun, verb) == 19690720):
            ans =  100 * noun + verb
            break

print(ans)