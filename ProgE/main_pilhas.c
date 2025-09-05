#include <stdio.h>
#include<stdlib.h>
#include"tad.c"

int main()
{
    pilha P;
    cria_pilha(&P, 10);

    push_pilha(&P, 8);
    push_pilha(&P, 5);
    push_pilha(&P, 77);
    push_pilha(&P, 1);
    push_pilha(&P, 2);
    imprime_pilha(&P);

    return 0;
}

