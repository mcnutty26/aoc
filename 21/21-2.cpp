#include <stdlib.h>
#include <stdio.h>
#include <unordered_set>

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
    int r[7] = {0,0,0,0,0,0,0};
    int (*opcodes[16])(int x, int y) = {addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr};

    const int len = 31;
    struct operation ops[len];
    int codes[len];
    codes[0] = 9;
    ops[0].a = 123;
    ops[0].b = 0;
    ops[0].c = 4;
    codes[1] = 5;
    ops[1].a = 4;
    ops[1].b = 456;
    ops[1].c = 4;
    codes[2] = 14;
    ops[2].a = 4;
    ops[2].b = 72;
    ops[2].c = 4;
    codes[3] = 0;
    ops[3].a = 4;
    ops[3].b = 1;
    ops[3].c = 1;
    codes[4] = 9;
    ops[4].a = 0;
    ops[4].b = 0;
    ops[4].c = 1;
    codes[5] = 9;
    ops[5].a = 0;
    ops[5].b = 8;
    ops[5].c = 4;
    codes[6] = 7;
    ops[6].a = 4;
    ops[6].b = 65536;
    ops[6].c = 3;
    codes[7] = 9;
    ops[7].a = 16098955;
    ops[7].b = 8;
    ops[7].c = 4;
    codes[8] = 5;
    ops[8].a = 3;
    ops[8].b = 255;
    ops[8].c = 5;
    codes[9] = 0;
    ops[9].a = 4;
    ops[9].b = 5;
    ops[9].c = 4;
    codes[10] = 5;
    ops[10].a = 4;
    ops[10].b = 16777215;
    ops[10].c = 4;
    codes[11] = 3;
    ops[11].a = 4;
    ops[11].b = 65899;
    ops[11].c = 4;
    codes[12] = 5;
    ops[12].a = 4;
    ops[12].b = 16777215;
    ops[12].c = 4;
    codes[13] = 10;
    ops[13].a = 256;
    ops[13].b = 3;
    ops[13].c = 5;
    codes[14] = 0;
    ops[14].a = 5;
    ops[14].b = 1;
    ops[14].c = 1;
    codes[15] = 1;
    ops[15].a = 1;
    ops[15].b = 1;
    ops[15].c = 1;
    codes[16] = 9;
    ops[16].a = 27;
    ops[16].b = 3;
    ops[16].c = 1;
    codes[17] = 9;
    ops[17].a = 0;
    ops[17].b = 7;
    ops[17].c = 5;
    codes[18] = 1;
    ops[18].a = 5;
    ops[18].b = 1;
    ops[18].c = 2;
    codes[19] = 3;
    ops[19].a = 2;
    ops[19].b = 256;
    ops[19].c = 2;
    codes[20] = 12;
    ops[20].a = 2;
    ops[20].b = 3;
    ops[20].c = 2;
    codes[21] = 0;
    ops[21].a = 2;
    ops[21].b = 1;
    ops[21].c = 1;
    codes[22] = 1;
    ops[22].a = 1;
    ops[22].b = 1;
    ops[22].c = 1;
    codes[23] = 9;
    ops[23].a = 25;
    ops[23].b = 1;
    ops[23].c = 1;
    codes[24] = 1;
    ops[24].a = 5;
    ops[24].b = 1;
    ops[24].c = 5;
    codes[25] = 9;
    ops[25].a = 17;
    ops[25].b = 6;
    ops[25].c = 1;
    codes[26] = 8;
    ops[26].a = 5;
    ops[26].b = 4;
    ops[26].c = 3;
    codes[27] = 9;
    ops[27].a = 7;
    ops[27].b = 5;
    ops[27].c = 1;
    codes[28] = 15;
    ops[28].a = 4;
    ops[28].b = 0;
    ops[28].c = 5;
    codes[29] = 0;
    ops[29].a = 5;
    ops[29].b = 1;
    ops[29].c = 1;
    codes[30] = 9;
    ops[30].a = 5;
    ops[30].b = 3;
    ops[30].c = 1;
	int lr4 = 0;
	std::unordered_set<int> r4s;
    do {

		if (ip == 28) {
			if (r4s.count(r[4])) {
				printf("%d", lr4);
				exit(0);
			} else {
				r4s.insert(r[4]);
				lr4 = r[4];
			}
		}

        r[1] = ip;
        if (codes[ip]==0||codes[ip]==2||codes[ip]==4||codes[ip]==6||codes[ip]==8||codes[ip]==12||codes[ip]==15){
            r[ops[ip].c] = (*opcodes[codes[ip]])(r[ops[ip].a], r[ops[ip].b]);
        }
        else if (codes[ip]==1||codes[ip]==3||codes[ip]==5||codes[ip]==7||codes[ip]==11||codes[ip]==14){
            r[ops[ip].c] = (*opcodes[codes[ip]])(r[ops[ip].a], ops[ip].b);
        }
        else {
            r[ops[ip].c] = (*opcodes[codes[ip]])(ops[ip].a, r[ops[ip].b]);
        }
        ip = r[1];
        ip++;
    } while (ip > 0 && ip < len);

    printf("[%d, %d, %d, %d, %d, %d]\n",r[0], r[1], r[2], r[3], r[4], r[5]);
    return 0;
}

