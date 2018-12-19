import sys

if len(sys.argv) != 2:
    print("Program takes a single argument (the input elf file)")
    sys.exit(1)

program = []

with open(sys.argv[1]) as f:
    for line in f: program.append(line.strip('\n').split(' '))

if program[0][0] == "#ip":
    ip_r = int(program.pop(0)[1])
else:
    ip_r = 6

start = """
#include <stdio.h>

int addr(int a, int b){return a + b;}
int addi(int a, int b){return a + b;}
int mulr(int a, int b){return a * b;}
int muli(int a, int b){return a * b;}
int banr(int a, int b){return a & b;}
int bani(int a, int b){return a & b;}
int borr(int a, int b){return a | b;}
int bori(int a, int b){return a | b;}
int setr(int a, int b){return a;}
int seti(int a, int b){return a;}
int gtir(int a, int b){return a > b;}
int gtri(int a, int b){return a > b;}
int gtrr(int a, int b){return a > b;}
int eqir(int a, int b){return a == b;
int eqri(int a, int b){return a == b;
int eqrr(int a, int b){return a == b;

int main()
{

    struct operation{
        int a;
        int b;
        int c;
    };
    
    int ip = 0;
    int r[7] = {0,0,0,0,0,0,0};
    int (*opcodes[16])(int x, int y) = {addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr};
"""

end = """
    printf("[%d, %d, %d, %d, %d, %d]\\n",r[0], r[1], r[2], r[3], r[4], r[5]);
    return 0;
}
"""

loop = f"""
    do {{
        r[{ip_r}] = ip;
        if (codes[ip]==0||codes[ip]==2||codes[ip]==4||codes[ip]==6||codes[ip]==8||codes[ip]==12||codes[ip]==15){{
            r[ops[ip].c] = (*opcodes[codes[ip]])(r[ops[ip].a], r[ops[ip].b]);
        }}
        else if (codes[ip]==1||codes[ip]==3||codes[ip]==5||codes[ip]==7||codes[ip]==11||codes[ip]==14){{
            r[ops[ip].c] = (*opcodes[codes[ip]])(r[ops[ip].a], ops[ip].b);
        }}
        else {{
            r[ops[ip].c] = (*opcodes[codes[ip]])(ops[ip].a, r[ops[ip].b]);
        }}
        ip = r[{ip_r}];
        ip++;
//        printf("%d, %d, %d, %d, %d, %d\\n",r[0], r[1], r[2], r[3], r[4], r[5]);
    }} while (ip > 0 && ip < len);"""

ops = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

print(start)
print(f"    const int len = {len(program)};")
print(f"    struct operation ops[len];")
print(f"    int codes[len];")

for i in range(len(program)):
    print(f"    codes[{i}] = {ops.index(program[i][0])};")
    print(f"    ops[{i}].a = {program[i][1]};")
    print(f"    ops[{i}].b = {program[i][2]};")
    print(f"    ops[{i}].c = {program[i][3]};")

print(loop)
print(end)
