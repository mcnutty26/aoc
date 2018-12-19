import sys

if len(sys.argv) != 2:
    print("Program takes a single argument (the input elf file)")
    sys.exit(1)

program = []

with open(sys.argv[1]) as f:
    for line in f: program.append(line.strip('\n').split(' '))

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
    int ip = 0;
    int r0 = 0;
    int r1 = 0;
    int r2 = 0;
    int r3 = 0;
    int r4 = 0;
    int r5 = 0;
"""

end = """
    printf("%d, %d, %d, %d, %d, %d\\n",r0, r1, r2, r3, r4, r5);
    return 0;
}
"""

print(start)
for i in program:
    if (i[0][0] == 'g' or i[0][0] == 'e') and not i[0][-2] == i[0][-1]:
        if i[0][-1] == 'r':
            print(f"    r{i[3]} = {i[0]}({i[1]}, r{i[2]});")
        else:
            print(f"    r{i[3]} = {i[0]}(r{i[1]}, {i[2]});")
    elif i[0][-1] == 'r':
        print(f"    r{i[3]} = {i[0]}(r{i[1]}, r{i[2]});")
    else:
        print(f"    r{i[3]} = {i[0]}(r{i[1]}, {i[2]});")
print(end)
