import sys

class intcode_vm:

    def __init__(self, program: list, input_queue: list, silent=False) -> None:
        self.program = dict()
        for token in program:
            self.program[len(self.program)] = token
        self.input_queue = input_queue
        self.output_queue = []
        self.halted = False
        self.rel_offset = 0
        self.ip = 0
        if not silent:
            print(">>> Booting nuttyIntcode Interpreter v1.4 <<<")

    def _get_data(self, mode: int, value: int) -> int:
        if mode == 0:
            return self.program.get(value, 0)
        elif mode == 1:
            return value
        elif mode == 2:
            return self.program.get(self.rel_offset + value, 0)
        else:
            print(f">>> ERROR: Illegal mode {mode} when accessing program at IP {self.ip} <<<")
            sys.exit(1)

    def _set_data(self, location: int, value: int, mode: int) -> None:
        if mode == 0:
            self.program[location] = value
        elif mode == 2:
            self.program[self.rel_offset + location] = value
        else:
            print(f">>> ERROR: Illegal mode {mode} when writing program at IP {self.ip} <<<")
            sys.exit(1)

    def _jit(self, a: int, b: int) -> None:
        if a != 0:
            self.ip = b
        else:
            self.ip += 3

    def _jif(self, a: int, b: int) -> None:
        if a == 0:
            self.ip = b
        else:
            self.ip += 3

    def _lt(self, a: int, b: int, c: int, mode: int) -> None:
        if a < b:
            self._set_data(c, 1, mode)
        else:
            self._set_data(c, 0, mode)

    def _eq(self, a: int, b: int, c: int, mode: int) -> None:
        if a == b:
            self._set_data(c, 1, mode)
        else:
            self._set_data(c, 0, mode)

    def run(self) -> list:
        self.output_queue = []
        while self.program[self.ip] != 99:

            ins = self.program[self.ip]
            opcode = ins % 10
            ins //= 100
            mode_1 = ins % 10
            ins //= 10
            mode_2 = ins % 10
            ins //= 10
            mode_3 = ins % 10

            if opcode == 1:
                self._set_data(self.program.get(self.ip + 3, 0), self._get_data(mode_1, self.program.get(self.ip + 1, 0)) + self._get_data(mode_2, self.program.get(self.ip + 2, 0)), mode_3)
                self.ip += 4
            elif opcode == 2:
                self._set_data(self.program.get(self.ip + 3, 0), self._get_data(mode_1, self.program.get(self.ip + 1, 0)) * self._get_data(mode_2, self.program.get(self.ip + 2, 0)), mode_3)
                self.ip += 4
            elif opcode == 3:
                if len(self.input_queue) == 0:
                    return self.output_queue
                self._set_data(self.program.get(self.ip + 1, 0), self.input_queue.pop(0), mode_1)
                self.ip += 2
            elif opcode == 4:
                self.output_queue.append(self._get_data(mode_1, self.program.get(self.ip + 1, 0)))
                self.ip += 2
            elif opcode == 5:
                self._jit(self._get_data(mode_1, self.program.get(self.ip + 1, 0)), self._get_data(mode_2, self.program.get(self.ip + 2, 0)))
            elif opcode == 6:
                self._jif(self._get_data(mode_1, self.program.get(self.ip + 1, 0)), self._get_data(mode_2, self.program.get(self.ip + 2, 0)))
            elif opcode == 7:
                self._lt(self._get_data(mode_1, self.program.get(self.ip + 1, 0)), self._get_data(mode_2, self.program.get(self.ip + 2, 0)), self.program.get(self.ip + 3, 0), mode_3)
                self.ip += 4
            elif opcode == 8:
                self._eq(self._get_data(mode_1, self.program.get(self.ip + 1, 0)), self._get_data(mode_2, self.program.get(self.ip + 2, 0)), self.program.get(self.ip + 3, 0), mode_3)
                self.ip += 4
            elif opcode == 9:
                self.rel_offset += self._get_data(mode_1, self.program.get(self.ip + 1, 0))
                self.ip += 2
            else:
                print(f">>> ERROR: Illegal opcode {opcode} at IP {self.ip} <<<")
                sys.exit(1)
        self.halted = True
        return self.output_queue
