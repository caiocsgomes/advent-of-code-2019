import csv

numbers = []
with open("day5-input.txt", "r") as f:
    numbers = [i for line in f for i in line.split(',')]

class Operation:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4

class Mode:
    POSITION = 0
    IMMEDIATE = 1

class IntructionParser:
    string_raw_instruction: str
    op_code: Operation
    parameter_mode_1: Mode
    parameter_mode_2: Mode
    parameter_mode_3: Mode
    instruction_size: int

    @staticmethod
    def parse(number: str):
        number_string = str(number)
        op_raw_code = number_string[-1]
        operation_type = ''

        if op_raw_code in ('3', '4'):
            instruction_size = 2
            op_code = Operation.INPUT if op_raw_code == '3' else Operation.OUTPUT
        else:
            instruction_size = 4
            op_code = Operation.MULTIPLY if op_raw_code == '1' else Operation.ADD
            parameter_mode_1 = Mode.POSITION if len(number_string) <= 2 else Mode.POSITION if number_string[-3] == '0' else Mode.IMMEDIATE
            parameter_mode_2 = Mode.POSITION if len(number_string) <= 3 else Mode.POSITION if number_string[-4] == '0' else Mode.IMMEDIATE
            parameter_mode_3 = Mode.POSITION if len(number_string) <= 4 else Mode.POSITION if number_string[-5] == '0' else Mode.IMMEDIATE

for number in numbers:
    instruction_parser = IntructionParser()
    instruction = instruction_parser.parse(number)