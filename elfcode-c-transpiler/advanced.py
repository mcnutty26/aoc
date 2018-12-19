import sys

if len(sys.argv) != 2:
    print("Program takes a single argument (the input elf file)")
    sys.exit(1)

program = []

with open(sys.argv[1]) as f:
    for line in f: program.append(line.strip('\n').split(' '))

ip_r = int(program.pop(0)[1])
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
int seti(int a, int b){return b;}
int gtir(int a, int b){return a > b;}
int gtri(int a, int b){return a > b;}
int gtrr(int a, int b){return a > b;}
int eqir(int a, int b){return a == b;}
int eqri(int a, int b){return a == b;}
int eqrr(int a, int b){return a == b;}

int main()
{

    struct operation{
        int a;
        int b;
        int c;
    };
    
    int ip = 0;
    int r[6] = {0,0,0,0,0,0};
    int (*opcodes[16])(int x, int y) = {addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr};
    
"""

end = """
    printf("%d, %d, %d, %d, %d, %d\\n",r[0], r[1], r[2], r[3], r[4], r[5]);
    return 0;
}
"""

loop = f"""
    for (int i = 0; i < len; i++) {{
        int a = ops[i].a;
        int b = ops[i].b;
        int c = ops[i].c;
        r[{ip_r}] = ip;
        r[c] = (*opcodes[codes[ip]])(a, b);
        ip = r[{ip_r}];
        ip++;
    }}"""

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
