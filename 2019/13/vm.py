import sys

class intcode_vm:
    program = []
    input_queue = []
    output_queue = []
    ip = 0
    halted = False
    rel_offset = 0

    def __init__(self, program, input_queue):
        self.program = program
        self.input_queue = input_queue
        self.output_queue = []
        self.halted = False
        self.rel_offset = 0
        print(">>> Booting nuttyIntcode Interpreter v1.4 <<<")

    def get_data(self, mode, value):
        if mode == 0:
            return self.mem(value)
        elif mode == 1:
            return value
        elif mode == 2:
            return self.mem(self.rel_offset + value)
        else:
            print(f">>> ERROR: Illegal mode {mode} when accessing program at IP {self.ip} <<<")
            sys.exit(1)

    def set_data(self, location, value, mode):
        if mode == 0:
            self.mem(location, value)
        elif mode == 2:
            self.mem(self.rel_offset + location, value)
        else:
            print(f">>> ERROR: Illegal mode {mode} when writing program at IP {self.ip} <<<")
            sys.exit(1)

    def mem(self, location, value=None):
        if location < 0:
            print(f">>> ERROR: Illegal address {location} at IP {self.ip} <<<")
            sys.exit(1)
        elif location >= len(self.program):
            while location >= len(self.program):
                self.program.append(0)
        if value == None:
            return self.program[location]
        else:
            self.program[location] = value

    def add(self, a, b, c, mode):
        self.set_data(c, a + b, mode)

    def mul(self, a, b, c, mode):
        self.set_data(c, a * b, mode)

    def io_in(self, a, mode):
        self.set_data(a, self.input_queue.pop(0), mode)

    def io_out(self, a):
        self.output_queue.append(a)

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

    def lt(self, a, b, c, mode):
        if a < b:
            self.set_data(c, 1, mode)
        else:
            self.set_data(c, 0, mode)

    def eq(self, a, b, c, mode):
        if a == b:
            self.set_data(c, 1, mode)
        else:
            self.set_data(c, 0, mode)

    def ofs(self, a):
        self.rel_offset += a

    def run(self):
        self.output_queue = []
        while self.mem(self.ip) != 99:
            ins = self.mem(self.ip)
            mode_1 = 0
            mode_2 = 0
            mode_3 = 0

            if ins == 0 or ins > 99999:
                print(f">>> ERROR: Illegal instruction {ins} at IP {self.ip} <<<")
                sys.exit(1)

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
                self.add(self.get_data(mode_1, self.mem(self.ip + 1)), self.get_data(mode_2, self.mem(self.ip + 2)), self.mem(self.ip + 3), mode_3)
                self.ip += 4
            elif opcode == 2:
                self.mul(self.get_data(mode_1, self.mem(self.ip + 1)), self.get_data(mode_2, self.mem(self.ip + 2)), self.mem(self.ip + 3), mode_3)
                self.ip += 4
            elif opcode == 3:
                if len(self.input_queue) == 0:
                    return self.output_queue
                self.io_in(self.mem(self.ip + 1), mode_1)
                self.ip += 2
            elif opcode == 4:
                self.io_out(self.get_data(mode_1, self.mem(self.ip + 1)))
                self.ip += 2
            elif opcode == 5:
                self.jit(self.get_data(mode_1, self.mem(self.ip + 1)), self.get_data(mode_2, self.mem(self.ip + 2)))
            elif opcode == 6:
                self.jif(self.get_data(mode_1, self.mem(self.ip + 1)), self.get_data(mode_2, self.mem(self.ip + 2)))
            elif opcode == 7:
                self.lt(self.get_data(mode_1, self.mem(self.ip + 1)), self.get_data(mode_2, self.mem(self.ip + 2)), self.mem(self.ip + 3), mode_3)
                self.ip += 4
            elif opcode == 8:
                self.eq(self.get_data(mode_1, self.mem(self.ip + 1)), self.get_data(mode_2, self.mem(self.ip + 2)), self.mem(self.ip + 3), mode_3)
                self.ip += 4
            elif opcode == 9:
                self.ofs(self.get_data(mode_1, self.mem(self.ip + 1)))
                self.ip += 2
            else:
                print(f">>> ERROR: Illegal opcode {opcode} at IP {self.ip} <<<")
                sys.exit(1)
        self.halted = True
        return self.output_queue
