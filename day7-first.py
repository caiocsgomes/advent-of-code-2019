import csv
import itertools

software_string = []
with open("day7-input.txt", "r") as f:
    software_string = [i for line in f for i in line.split(',')]


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

    def get_param(self, parameter_position: int, pointer: int, software):
        return (software[pointer + parameter_position]
                if self.modes[parameter_position - 1] == Mode.IMMEDIATE
                else software[software[pointer + parameter_position]])


class InstructionParser:
    @staticmethod
    def parse(number: int):
        number_string = str(number)
        op_code = int(number_string[-1])
        parameter_mode_1 = (Mode.POSITION
                            if len(number_string) <= 2
                            else Mode.POSITION
                                if number_string[-3] == '0'
                                else Mode.IMMEDIATE)
        if op_code in (3, 4):
            instruction_size = 2
            return Instruction(op_code, parameter_mode_1, None, None, instruction_size)
        else:
            instruction_size = 4 if op_code not in (5, 6) else 3
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
software_numbers = list(map(int, software_string))


def intcode_run_amplifier(phase_amp, software, input_amp=0, use_phase = True, pointer = 0, feeback_mode = False, output = 0):
    while pointer < len(software):
        instruction = instruction_parser.parse(software[pointer])

        if instruction.op_code == Operation.ADD:
            if instruction.parameter_mode_3 == Mode.IMMEDIATE:
                software[pointer + 3] = instruction.get_param(1, pointer, software) \
                                        + instruction.get_param(2, pointer, software)
            else:
                software[software[pointer + 3]] = instruction.get_param(1, pointer, software)\
                                                  + instruction.get_param(2, pointer, software)
            pointer += instruction.instruction_size

        elif instruction.op_code == Operation.MULTIPLY:
            if instruction.parameter_mode_3 == Mode.IMMEDIATE:
                software[pointer + 3] = instruction.get_param(1, pointer, software) \
                                        * instruction.get_param(2, pointer, software)
            else:
                software[software[pointer + 3]] = instruction.get_param(1, pointer, software) \
                                                  * instruction.get_param(2, pointer, software)
            pointer += instruction.instruction_size

        elif instruction.op_code == Operation.INPUT:
            if instruction.parameter_mode_1 == Mode.IMMEDIATE:
                if use_phase:
                    use_phase = False
                    software[pointer + 1] = phase_amp
                else:
                    software[pointer + 1] = input_amp
            else:
                if use_phase:
                    use_phase = False
                    software[software[pointer + 1]] = phase_amp
                else:
                    software[software[pointer + 1]] = input_amp

            pointer += instruction.instruction_size

        elif instruction.op_code == Operation.OUTPUT:
            output = software[pointer + 1] \
                if instruction.parameter_mode_1 == Mode.IMMEDIATE \
                else software[software[pointer + 1]]
            pointer += instruction.instruction_size

        elif instruction.op_code == Operation.JUMP_IF_TRUE:
            pointer = instruction.get_param(2, pointer, software) \
                if instruction.get_param(1, pointer, software) != 0 \
                else pointer + instruction.instruction_size

        elif instruction.op_code == Operation.JUMP_IF_FALSE:
            pointer = instruction.get_param(2, pointer, software) \
                if instruction.get_param(1, pointer, software) == 0 \
                else pointer + instruction.instruction_size

        elif instruction.op_code == Operation.LESS_THAN:
            software[software[pointer + 3]] = 1 \
                if instruction.get_param(1, pointer) < instruction.get_param(2, pointer, software) \
                else 0
            pointer += instruction.instruction_size

        elif instruction.op_code == Operation.EQUALS:
            software[software[pointer + 3]] = 1 \
                if instruction.get_param(1, pointer, software) == instruction.get_param(2, pointer, software) \
                else 0
            pointer += instruction.instruction_size

        elif instruction.op_code == Operation.HALT:
            return output, True, pointer

        else:
            raise Exception("Not this time buddy")

    return output, False, pointer


perms_1 = list(itertools.permutations(range(5)))
softwares = [software_numbers[:]] * 5
thrusters_signal_1 = []
pointer = 0
for perm in perms_1:
    input_amp = 0
    halt = False
    for i, phase in enumerate(perm):
        input_amp, _, _ = intcode_run_amplifier(phase, softwares[i], input_amp)
    thrusters_signal_1.append(input_amp)

print("Part1: ", max(thrusters_signal_1))
