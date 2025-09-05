// Definição do TAD para listas duplamente encadeadas circular

struct NO
{
	int info;
	struct NO *prox, *ant;
};
typedef struct NO lista;

lista * aloca_no(void)
{
    lista *aux;
    aux       = (lista *) malloc (sizeof(lista));
    aux->prox = aux;
    aux->ant  = aux;

    return aux;
}

void imprime_lista_DC(lista* L)
{
    lista* no = L;

    if (L == NULL)
    {
        printf("L = vazio");
        return;
    }

    printf("L = ");
    do
    {
        printf("%d, ", no->info);
        no = no->prox;
    }
    while (no != L);

    printf("\n");
}


lista * exclui_lista_DC (lista* L)
{
    lista* no = L;

    // Lista vazia
    if (L == NULL)
        return L;

    do
    {
        lista* temp = no->prox;
        free(no);
        no         = temp;
    }while (no != L);

    return NULL;
}


lista* insere_lista_pos_DC(lista* L, int el, int pos)
{
    if(pos < 0)
    {
       printf("Posicao invalida\n");
       return L;
    }
    // insercao no inicio
    if (L == NULL)
    {
        lista *no;
        no        = aloca_no();
        no->info  = el;
        no->prox  = no;
        no->ant   = no;
        return no;
    }
    // posicao inicial (cabeca)
    else if (pos == 0)
    {
        lista *no;
        no        = aloca_no();
        no->info  = el;

        lista * ultimo = L->ant;
        no->prox       = L;
		no->ant        = ultimo;
		L->ant         = no;
		ultimo->prox   = no;

        return no;
    }
    // demais posicoes
    else
    {
        lista * anterior = L;

        // encontra anterior do elemento (se existir)
        for(int i=0; i<pos-1; i++)
        {
            anterior=anterior->prox;

            // passou do fim
            if (anterior == L)
            {
                printf("Posicao invalida\n");
                return L;
            }
        }

        lista *novo         = aloca_no();
        novo->info          = el;
        novo->prox          = anterior->prox;
        novo->ant           = anterior;
        anterior->prox->ant = novo;
        anterior->prox      = novo;

        return L;
    }
}





