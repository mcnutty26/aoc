
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
    

    const int len = 36;
    struct operation ops[len];
    int codes[len];
    codes[0] = 1;
    ops[0].a = 3;
    ops[0].b = 16;
    ops[0].c = 3;
    codes[1] = 9;
    ops[1].a = 1;
    ops[1].b = 3;
    ops[1].c = 1;
    codes[2] = 9;
    ops[2].a = 1;
    ops[2].b = 2;
    ops[2].c = 4;
    codes[3] = 2;
    ops[3].a = 1;
    ops[3].b = 4;
    ops[3].c = 5;
    codes[4] = 15;
    ops[4].a = 5;
    ops[4].b = 2;
    ops[4].c = 5;
    codes[5] = 0;
    ops[5].a = 5;
    ops[5].b = 3;
    ops[5].c = 3;
    codes[6] = 1;
    ops[6].a = 3;
    ops[6].b = 1;
    ops[6].c = 3;
    codes[7] = 0;
    ops[7].a = 1;
    ops[7].b = 0;
    ops[7].c = 0;
    codes[8] = 1;
    ops[8].a = 4;
    ops[8].b = 1;
    ops[8].c = 4;
    codes[9] = 12;
    ops[9].a = 4;
    ops[9].b = 2;
    ops[9].c = 5;
    codes[10] = 0;
    ops[10].a = 3;
    ops[10].b = 5;
    ops[10].c = 3;
    codes[11] = 9;
    ops[11].a = 2;
    ops[11].b = 6;
    ops[11].c = 3;
    codes[12] = 1;
    ops[12].a = 1;
    ops[12].b = 1;
    ops[12].c = 1;
    codes[13] = 12;
    ops[13].a = 1;
    ops[13].b = 2;
    ops[13].c = 5;
    codes[14] = 0;
    ops[14].a = 5;
    ops[14].b = 3;
    ops[14].c = 3;
    codes[15] = 9;
    ops[15].a = 1;
    ops[15].b = 0;
    ops[15].c = 3;
    codes[16] = 2;
    ops[16].a = 3;
    ops[16].b = 3;
    ops[16].c = 3;
    codes[17] = 1;
    ops[17].a = 2;
    ops[17].b = 2;
    ops[17].c = 2;
    codes[18] = 2;
    ops[18].a = 2;
    ops[18].b = 2;
    ops[18].c = 2;
    codes[19] = 2;
    ops[19].a = 3;
    ops[19].b = 2;
    ops[19].c = 2;
    codes[20] = 3;
    ops[20].a = 2;
    ops[20].b = 11;
    ops[20].c = 2;
    codes[21] = 1;
    ops[21].a = 5;
    ops[21].b = 8;
    ops[21].c = 5;
    codes[22] = 2;
    ops[22].a = 5;
    ops[22].b = 3;
    ops[22].c = 5;
    codes[23] = 1;
    ops[23].a = 5;
    ops[23].b = 6;
    ops[23].c = 5;
    codes[24] = 0;
    ops[24].a = 2;
    ops[24].b = 5;
    ops[24].c = 2;
    codes[25] = 0;
    ops[25].a = 3;
    ops[25].b = 0;
    ops[25].c = 3;
    codes[26] = 9;
    ops[26].a = 0;
    ops[26].b = 5;
    ops[26].c = 3;
    codes[27] = 8;
    ops[27].a = 3;
    ops[27].b = 0;
    ops[27].c = 5;
    codes[28] = 2;
    ops[28].a = 5;
    ops[28].b = 3;
    ops[28].c = 5;
    codes[29] = 0;
    ops[29].a = 3;
    ops[29].b = 5;
    ops[29].c = 5;
    codes[30] = 2;
    ops[30].a = 3;
    ops[30].b = 5;
    ops[30].c = 5;
    codes[31] = 3;
    ops[31].a = 5;
    ops[31].b = 14;
    ops[31].c = 5;
    codes[32] = 2;
    ops[32].a = 5;
    ops[32].b = 3;
    ops[32].c = 5;
    codes[33] = 0;
    ops[33].a = 2;
    ops[33].b = 5;
    ops[33].c = 2;
    codes[34] = 9;
    ops[34].a = 0;
    ops[34].b = 8;
    ops[34].c = 0;
    codes[35] = 9;
    ops[35].a = 0;
    ops[35].b = 9;
    ops[35].c = 3;

    for (int i = 0; i < len; i++) {
        int a = ops[i].a;
        int b = ops[i].b;
        int c = ops[i].c;
        r[3] = ip;
        r[c] = (*opcodes[codes[ip]])(a, b);
        ip = r[3];
        ip++;
    }

    printf("%d, %d, %d, %d, %d, %d\n",r[0], r[1], r[2], r[3], r[4], r[5]);
    return 0;
}

