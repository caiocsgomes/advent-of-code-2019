# https://stackoverflow.com/questions/339007/how-to-pad-zeroes-to-a-string
# https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement

class IntcodeMachine:
    def __init__(self, s):
        self._soft = list(map(int, s)) + [0] * 100000
        self._ptr = 0
        self._out = []
        self.inp = None
        self._halt = False
        self._started = False
        self._rel_base = 0

    def out(self):
        return self._out

    def halted(self):
        return self._halt

    def started(self):
        return self._started

    def reset_software(self, s):
        self._soft = list(map(int, s)) + [0] * 100000
        self._ptr = 0
        self._out = 0
        self._started = False
        self._rel_base = 0

    def add(self, val1, val2, out_pos):
        self._soft[out_pos] = val1 + val2
        self._ptr += 4

    def multiply(self, val1, val2, out_pos):
        self._soft[out_pos] = val1 * val2
        self._ptr += 4

    def input(self, inp, pos):
        self._soft[pos] = inp
        self.inp = None
        self._ptr += 2

    def output(self, val):
        self._out.append(val)
        self._ptr += 2

    def jump_if_true(self, val1, val2):
        if val1 != 0:
            self._ptr = val2
        else:
            self._ptr += 3

    def jump_if_false(self, val1, val2):
        if val1 == 0:
            self._ptr = val2
        else:
            self._ptr += 3

    def equals(self, val1, val2, pos):
        if val1 == val2:
            self._soft[pos] = 1
        else:
            self._soft[pos] = 0
        self._ptr += 4

    def less_than(self, val1, val2, pos):
        if val1 < val2:
            self._soft[pos] = 1
        else:
            self._soft[pos] = 0
        self._ptr += 4

    def rel_base(self, val):
        self._rel_base += val
        self._ptr += 2

    def execute(self, inp):
        self.inp = inp
        self._out = []
        while self._ptr < len(self._soft):
            self._started = True
            instr = self._soft[self._ptr]
            op = instr % 100
            # HALT
            if op == 99:
                self._halt = True
                break
            # MODES
            # 0: POSITION 1: IMMEDIATE 2: RELATIVE
            mod1, mod2, mod3 = (instr // 100) % 10, (instr // 1000) % 10, instr // 10000
            # VALUES AT ARGUMENTS POSITIONS
            a1, a2, a3 = self._soft[self._ptr + 1], self._soft[self._ptr + 2], self._soft[self._ptr + 3]
            if mod1 == 0:
                p1 = a1
            elif mod1 == 1:
                p1 = self._ptr + 1
            else:
                p1 = self._rel_base + a1
            v1 = self._soft[p1]
            if op not in {3, 4, 9}:  # modes that don't need p2
                if mod2 == 0:
                    p2 = a2
                elif mod2 == 1:
                    p2 = self._ptr + 2
                else:
                    p2 = self._rel_base + a2
                v2 = self._soft[p2]
            if op in {1, 2, 7, 8}:  # modes that need p3
                if mod3 == 0:
                    p3 = a3
                elif mod3 == 1:
                    p3 = self._ptr + 3
                else:
                    p3 = self._rel_base + a3
                v3 = self._soft[p3]

            if op == 1:
                self.add(v1, v2, p3)
            elif op == 2:
                self.multiply(v1, v2, p3)
            elif op == 3:
                if self.inp is None:
                    break
                self.input(self.inp, p1)
            elif op == 4:
                self.output(v1)
            elif op == 5:
                self.jump_if_true(v1, v2)
            elif op == 6:
                self.jump_if_false(v1, v2)
            elif op == 7:
                self.less_than(v1, v2, p3)
            elif op == 8:
                self.equals(v1, v2, p3)
            elif op == 9:
                self.rel_base(v1)
            else:
                raise Exception("Not this time buddy")
