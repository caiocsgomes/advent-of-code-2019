start = 124075
end = 580769

def validade_number_part1(number):
    two_adjacent_equals = False
    incremental = True
    string_number = str(number)
    for i in range(len(string_number) - 1):
        if string_number[i] == string_number[i + 1]:
            two_adjacent_equals = True
        if string_number[i] > string_number[i + 1]:
            incremental = False
    return two_adjacent_equals and incremental

count = 0

for i in range(start, end + 1):
    if validade_number_part1(i):
        count += 1

print("Part1: ",count)

def validade_number_part2(number):
    two_adjacent_equals = False
    incremental = True
    string_number = str(number)
    for i in range(len(string_number) - 1):
        if string_number[i] == string_number[i + 1]:
            if i == 0:
                two_adjacent_equals = string_number[i + 1] != string_number[i + 2] or two_adjacent_equals
            elif i == 4:
                two_adjacent_equals = string_number[i] != string_number[i - 1] or two_adjacent_equals
            else:
                two_adjacent_equals = (string_number[i - 1] != string_number[i]) and (string_number[i + 1] != string_number[i + 2]) or two_adjacent_equals
        if string_number[i] > string_number[i + 1]:
            incremental = False

    return two_adjacent_equals and incremental

count = 0

for i in range(start, end + 1):
    if validade_number_part2(i):
        count += 1

print("Part2: ",count)
