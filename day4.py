start = 124075
end = 580769


def validade_number_part1(number):
    list_number = list(str(number))
    two_adjacent_equals = any(list_number[i] == list_number[i+1] for i in range(len(list_number)-1))
    incremental = all(list_number[i] <= list_number[i+1] for i in range(len(list_number)-1))
    return two_adjacent_equals and incremental

count = 0

for i in range(start, end + 1):
    if validade_number_part1(i):
        count += 1

print("Part1: ", count)


def validade_number_part2(number):
    list_number = list(str(number))
    two_adjacent_equals = False
    incremental = all(list_number[i] <= list_number[i+1] for i in range(len(list_number)-1))
    
    for i in range(len(list_number) - 1):
        if list_number[i] == list_number[i + 1]:
            if i == 0:
                two_adjacent_equals = (
                    list_number[i + 1] != list_number[i + 2] 
                    or two_adjacent_equals)
            elif i == 4:
                two_adjacent_equals = (
                    list_number[i] != list_number[i - 1] 
                    or two_adjacent_equals)
            else:
                two_adjacent_equals = (
                    (list_number[i - 1] != list_number[i]) 
                    and (list_number[i + 1] != list_number[i + 2]) 
                    or two_adjacent_equals)

    return two_adjacent_equals and incremental


count = 0

for i in range(start, end + 1):
    if validade_number_part2(i):
        count += 1

print("Part2: ", count)
