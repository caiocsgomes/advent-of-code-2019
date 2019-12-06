import csv

numbers_string = []
with open("day5-input.txt", "r") as f:
    numbers_string = [i for line in f for i in line.split(',')]

class Operation:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 9

class Mode:
    POSITION = 0
    IMMEDIATE = 1

class Intruction:
    string_raw_instruction: str
    op_code: Operation
    parameter_mode_1: Mode
    parameter_mode_2: Mode
    parameter_mode_3: Mode
    instruction_size: int

class InstructionParser:
    @staticmethod
    def parse(number: int):
        number_string = str(number)
        instruction = Intruction()
        instruction.op_code = int(number_string[-1])
        if instruction.op_code in (3, 4):
            instruction.instruction_size = 2
            instruction.parameter_mode_1 = Mode.POSITION if len(number_string) <= 2 else Mode.POSITION if number_string[-3] == '0' else Mode.IMMEDIATE
        else:
            instruction.instruction_size = 4
            instruction.parameter_mode_1 = Mode.POSITION if len(number_string) <= 2 else Mode.POSITION if number_string[-3] == '0' else Mode.IMMEDIATE
            instruction.parameter_mode_2 = Mode.POSITION if len(number_string) <= 3 else Mode.POSITION if number_string[-4] == '0' else Mode.IMMEDIATE
            instruction.parameter_mode_3 = Mode.POSITION if len(number_string) <= 4 else Mode.POSITION if number_string[-5] == '0' else Mode.IMMEDIATE
        return instruction

instruction_parser = InstructionParser()
input = 1
output = 0
pointer = 0
numbers = list(map(int, numbers_string))

while True:
    instruction = instruction_parser.parse(numbers[pointer])

    if instruction.op_code == Operation.ADD:
        first_argument = numbers[pointer + 1] if instruction.parameter_mode_1 == Mode.IMMEDIATE else numbers[numbers[pointer + 1]]
        second_argument = numbers[pointer + 2] if instruction.parameter_mode_2 == Mode.IMMEDIATE else numbers[numbers[pointer + 2]]
        result = first_argument + second_argument
        if (instruction.parameter_mode_3 == Mode.IMMEDIATE):
            numbers[pointer + 3] = result
        else:
            numbers[numbers[pointer + 3]] = result
        pointer += instruction.instruction_size
        
    elif instruction.op_code == Operation.MULTIPLY:
        first_argument = numbers[pointer + 1] if instruction.parameter_mode_1 == Mode.IMMEDIATE else numbers[numbers[pointer + 1]]
        second_argument = numbers[pointer + 2] if instruction.parameter_mode_2 == Mode.IMMEDIATE else numbers[numbers[pointer + 2]]
        result = first_argument * second_argument
        if (instruction.parameter_mode_3 == Mode.IMMEDIATE):
            numbers[pointer + 3] = result
        else:
            numbers[numbers[pointer + 3]] = result
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.INPUT:
        if (instruction.parameter_mode_1 == Mode.IMMEDIATE):
            numbers[pointer + 1] = input
        else:
            numbers[numbers[pointer + 1]] = input
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.OUTPUT:
        if (instruction.parameter_mode_1 == Mode.IMMEDIATE):
            output = numbers[pointer + 1]
        else:
            output = numbers[numbers[pointer + 1]]
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.HALT:
        break

    else:
        print ("Not this time buddy")
    print(output)

print(output)
