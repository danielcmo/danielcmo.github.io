#include <stdio.h>
#include<stdlib.h>
#include"tad.c"

int main()
{
    lista *L = NULL;

    L = insere_lista_pos_DC(L, 2, 0);
    L = insere_lista_pos_DC(L, 6, 1);
    L = insere_lista_pos_DC(L, 7, 1);
    L = insere_lista_pos_DC(L, 8, 2);
    L = insere_lista_pos_DC(L, 20, 4);
    imprime_lista_DC(L);

    exclui_lista_DC(L);
    return 0;
}
