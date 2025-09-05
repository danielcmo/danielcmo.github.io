// Definição do TAD para listas

struct NO
{
	int info;
	struct NO *prox;
};
typedef struct NO lista;

lista * aloca_no(void)
{
    lista *aux;
    aux       = (lista *) malloc (sizeof(lista));
    aux->prox = NULL;

    return aux;
}


lista * insere_lista(lista* L, int el)
{
    lista *no;
    no        = aloca_no();
    no->info  = el;
    no->prox  = L;
    L         = no;

    return L;
}


lista * exclui_lista (lista* L)
{
    lista* no = L;
    while (no != NULL)
    {
        lista* temp = no->prox;
        free(no);
        no         = temp;
    }

    return NULL;
}

void imprime_lista(lista* L)
{
    lista* no = L;

    printf("L = ");
    while (no != NULL)
    {
        printf("%d, ", no->info);
        no = no->prox;
    }
    printf("\n");
}




