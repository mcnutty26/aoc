class intcode_vm:
    program = []
    input_queue = []
    output_queue = []
    ip = 0
    halted = False

    def __init__(self, program, input_queue):
        self.program = program
        self.input_queue = input_queue
        self.output_queue = []
        self.halted = False

    def get_data(self, mode, value):
        if mode == 0:
            return self.program[value]
        elif mode == 1:
            return value

    def add(self, a, b, c):
        self.program[c] = a + b

    def mul(self, a, b, c):
        self.program[c] = a * b

    def io_in(self, a):
        self.program[a] = self.input_queue.pop(0)

    def io_out(self, a):
        self.output_queue.append([a])

    def jit(self, a, b):
        if a != 0:
            self.ip = b
        else:
            self.ip += 3

    def jif(self, a, b):
        if a == 0:
            self.ip = b
        else:
            self.ip += 3

    def lt(self, a, b, c):
        if a < b:
            self.program[c] = 1
        else:
            self.program[c] = 0

    def eq(self, a, b, c):
        if a == b:
            self.program[c] = 1
        else:
            self.program[c] = 0

    def run(self):
        while self.program[self.ip] != 99:
            ins = self.program[self.ip]
            mode_1 = 0
            mode_2 = 0
            mode_3 = 0

            if ins < 99:
                opcode = ins
            else:
                opcode = int(str(ins)[-2] + str(ins)[-1])

            if ins > 99:
                mode_1 = int(str(ins)[-3])
            if ins > 999:
                mode_2 = int(str(ins)[-4])
            if ins > 9999:
                mode_3 = int(str(ins)[-5])

            if opcode == 1:
                self.add(self.get_data(mode_1, self.program[self.ip + 1]), self.get_data(mode_2, self.program[self.ip + 2]), self.program[self.ip + 3])
                self.ip += 4
            elif opcode == 2:
                self.mul(self.get_data(mode_1, self.program[self.ip + 1]), self.get_data(mode_2, self.program[self.ip + 2]), self.program[self.ip + 3])
                self.ip += 4
            elif opcode == 3:
                if len(self.input_queue) == 0:
                    return self.output_queue.pop()
                self.io_in(self.program[self.ip + 1])
                self.ip += 2
            elif opcode == 4:
                self.io_out(self.get_data(mode_1, self.program[self.ip + 1]))
                self.ip += 2
            elif opcode == 5:
                self.jit(self.get_data(mode_1, self.program[self.ip + 1]), self.get_data(mode_2, self.program[self.ip + 2]))
            elif opcode == 6:
                self.jif(self.get_data(mode_1, self.program[self.ip + 1]), self.get_data(mode_2, self.program[self.ip + 2]))
            elif opcode == 7:
                self.lt(self.get_data(mode_1, self.program[self.ip + 1]), self.get_data(mode_2, self.program[self.ip + 2]), self.program[self.ip + 3])
                self.ip += 4
            elif opcode == 8:
                self.eq(self.get_data(mode_1, self.program[self.ip + 1]), self.get_data(mode_2, self.program[self.ip + 2]), self.program[self.ip + 3])
                self.ip += 4
            else:
                print("FAULT", opcode)
                return False
        self.halted = True
        return self.output_queue[0]
