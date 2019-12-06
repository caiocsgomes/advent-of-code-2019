import csv

numbers_string = []
with open("day5-input.txt", "r") as f:
    numbers_string = [i for line in f for i in line.split(',')]

class Operation:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 9

class Mode:
    POSITION = 0
    IMMEDIATE = 1

class Instruction:
    def __init__(self, op_code: Operation, parameter_mode_1: Mode, 
                parameter_mode_2: Mode, parameter_mode_3: Mode, 
                instruction_size: int):
        self.op_code = op_code
        self.parameter_mode_1 = parameter_mode_1
        self.parameter_mode_2 = parameter_mode_2
        self.parameter_mode_3 = parameter_mode_3
        self.instruction_size = instruction_size
        self.modes = [self.parameter_mode_1, self.parameter_mode_2, self.parameter_mode_3]

    def get_param(self, parameter_position: int):
        return (numbers[pointer + parameter_position] 
                if self.modes[parameter_position - 1] == Mode.IMMEDIATE 
                else numbers[numbers[pointer + parameter_position]])

class InstructionParser:
    @staticmethod
    def parse(number: int):
        number_string = str(number)
        op_code = int(number_string[-1])
        if op_code in (3, 4):
            instruction_size = 2
            parameter_mode_1 = (Mode.POSITION 
                                if len(number_string) <= 2 
                                else Mode.POSITION 
                                    if number_string[-3] == '0' 
                                    else Mode.IMMEDIATE)
            return Instruction(op_code, parameter_mode_1, None, None, instruction_size)
        else:
            instruction_size = 4 if op_code not in (5, 6) else 3
            parameter_mode_1 = (Mode.POSITION 
                                if len(number_string) <= 2 
                                else Mode.POSITION 
                                    if number_string[-3] == '0' 
                                    else Mode.IMMEDIATE)
            parameter_mode_2 = (Mode.POSITION 
                                if len(number_string) <= 3 
                                else Mode.POSITION 
                                    if number_string[-4] == '0' 
                                    else Mode.IMMEDIATE)
            parameter_mode_3 = (Mode.POSITION 
                                if len(number_string) <= 4 
                                else Mode.POSITION 
                                    if number_string[-5] == '0' 
                                    else Mode.IMMEDIATE)
            return Instruction(op_code, parameter_mode_1, 
                            parameter_mode_2, parameter_mode_3,
                            instruction_size)

instruction_parser = InstructionParser()
input = 5
output = 0
pointer = 0
numbers = list(map(int, numbers_string))

while True:
    instruction = instruction_parser.parse(numbers[pointer])

    if instruction.op_code == Operation.ADD:
        if (instruction.parameter_mode_3 == Mode.IMMEDIATE):
            numbers[pointer + 3] = instruction.get_param(1) + instruction.get_param(2)
        else:
            numbers[numbers[pointer + 3]] = instruction.get_param(1) + instruction.get_param(2)
        pointer += instruction.instruction_size
        
    elif instruction.op_code == Operation.MULTIPLY:
        if (instruction.parameter_mode_3 == Mode.IMMEDIATE):
            numbers[pointer + 3] = instruction.get_param(1) * instruction.get_param(2)
        else:
            numbers[numbers[pointer + 3]] = instruction.get_param(1) * instruction.get_param(2)
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.INPUT:
        if (instruction.parameter_mode_1 == Mode.IMMEDIATE):
            numbers[pointer + 1] = input
        else:
            numbers[numbers[pointer + 1]] = input
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.OUTPUT:
        output = numbers[pointer + 1] if instruction.parameter_mode_1 == Mode.IMMEDIATE else numbers[numbers[pointer + 1]]
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.JUMP_IF_TRUE:   
        pointer = instruction.get_param(2) if instruction.get_param(1)  != 0 else pointer + instruction.instruction_size

    elif instruction.op_code == Operation.JUMP_IF_FALSE:     
        pointer = instruction.get_param(2) if instruction.get_param(1) == 0 else pointer + instruction.instruction_size
        
    elif instruction.op_code == Operation.LESS_THAN:
        numbers[numbers[pointer + 3]] = 1 if instruction.get_param(1)  < instruction.get_param(2)  else 0
        pointer += instruction.instruction_size
        
    elif instruction.op_code == Operation.EQUALS:
        numbers[numbers[pointer + 3]] = 1 if instruction.get_param(1)  == instruction.get_param(2) else 0
        pointer += instruction.instruction_size

    elif instruction.op_code == Operation.HALT:
        break

    else:
        raise ("Not this time buddy")

    print(output)