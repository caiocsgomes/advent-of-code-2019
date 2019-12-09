class IntcodeMachine:
    def __init__(self, s):
        self._soft = s
        self._ptr = 0
        self.out = 0
        self._halt = False
        self._started = False
        self._rel_base = 0

    def output(self):
        return self.out

    def halted(self):
        return self._halt

    def started(self):
        return self._started

    def execute(self, inp):
        while self._ptr < len(self._soft):
            self._started = True
            instr = self._soft[self._ptr]
            op = int(instr[-1]) if len(instr) == 1 else int(instr[-2:])
            if op == 99:
                self._halt = True
                break
            mod3 = 0 if len(instr) <= 4 else int(instr[-5])
            # MODES
            mod2 = 0 if len(instr) <= 3 else int(instr[-4])
            mod1 = 0 if len(instr) <= 2 else int(instr[-3])
            p1 = int(self._soft[self._ptr + 1])
            # 0: POSITION 1: IMMEDIATE
            if mod1 == 0:
                par1 = int(self._soft[p1])
            elif mod1 == 2:
                par1 = int(self._soft[p1 + self._rel_base])
            else:
                par1 = p1
            if op not in {99, 3, 4, 9}:  # modes that don't need p2
                p2 = int(self._soft[self._ptr + 2])
                if mod2 == 0:
                    par2 = int(self._soft[p2])
                elif mod2 == 2:
                    par2 = int(self._soft[p2 + self._rel_base])
                else:
                    par2 = p2
            if op in {1, 2, 7, 8}:  # modes that need par3
                p3 = int(self._soft[self._ptr + 3])
                if mod3 == 0:
                    par3 = int(self._soft[p3])
                elif mod3 == 2:
                    par3 = int(self._soft[p3 + self._rel_base])
                else:
                    par3 = p3

            # ADD
            if op == 1:
                if mod3 == 1:
                    self._soft[self._ptr + 3] = par1 + par2
                elif mod3 == 2:
                    self._soft[self._ptr + self._rel_base + 3] = par1 + par2
                else:
                    self._soft[p3] = par1 + par2
                self._ptr += 4
            # MULTIPLY
            elif op == 2:
                if mod3 == 1:
                    self._soft[self._ptr + 3] = par1 * par2
                elif mod3 == 2:
                    self._soft[self._ptr + self._rel_base + 3] = par1 * par2
                else:
                    self._soft[p3] = par1 * par2
                self._ptr += 4
            # INPUT
            elif op == 3:
                if inp is None:
                    # input already used
                    break

                self._soft[p1] = inp
                inp = None
                self._ptr += 2
            # OUTPUT
            elif op == 4:
                if mod1 == 1:
                    self.out = p1
                elif mod1 == 2:
                    self.out = self._soft[p1 + self._rel_base]
                else:
                    self.out = self._soft[p1]
                self._ptr += 2
            # JUMP_IF_TRUE
            elif op == 5:
                if par1 != 0:
                    self._ptr = par2
                else:
                    self._ptr += 3
            # JUMP_IF_FALSE
            elif op == 6:
                if par1 == 0:
                    self._ptr = par2
                else:
                    self._ptr += 3
            # LESS_THAN
            elif op == 7:
                if par1 < par2:
                    self._soft[par3] = 1
                else:
                    self._soft[par3] = 0
                self._ptr += 4
            # EQUALS
            elif op == 8:
                if par1 == par2:
                    self._soft[par3] = 1
                else:
                    self._soft[par3] = 0
                self._ptr += 4
            # RELATIVE BASE
            elif op == 9:
                if mod1 == 1:
                    self._rel_base = p1
                elif mod1 == 2:
                    self._rel_base = self._soft[p1 + self._rel_base]
                else:
                    self._rel_base = self._soft[p1]
                self._ptr += 2
            else:
                raise Exception("Not this time buddy")
