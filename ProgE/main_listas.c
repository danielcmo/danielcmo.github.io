#include <stdio.h>
#include<stdlib.h>
#include"tad_listas.c"

int main()
{
    int k;

    lista *L = NULL;
    L = insere_lista(L, 5);
    L = insere_lista(L, 4);
    L = insere_lista(L, 3);
    L = insere_lista(L, 4);
    L = insere_lista(L, 5);
    imprime_lista(L);

    L = exclui_lista (L);

    return 0;
}

