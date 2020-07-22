LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010
ADD = 0b10100000
SUB = 0b10100001

        self.branchtable = {}
        self.branchtable[LDI] = self.LDI
        self.branchtable[HLT] = self.HLT
        self.branchtable[PRN] = self.PRN
        self.branchtable[MUL] = self.MUL
        self.branchtable[ADD] = self.ADD
        self.branchtable[SUB] = self.SUB

        self.branchtable = {
            0b10000010: self.LDI,
            0b00000001: self.HLT,
            0b01000111: self.PRN,
            0b10100010: self.MUL,
            0b10100000: self.ADD,
            0b10100001: self.SUB

        }
