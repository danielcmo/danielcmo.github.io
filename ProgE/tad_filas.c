

// ******************************** Definição do TAD para Pilha em vetores  *************************

struct PILHA
{
  int tam;
  int topo;
  int *v;
};
typedef struct PILHA pilha;


void cria_pilha(pilha * P, int tam)
{
    P->topo = -1;
    P->tam  = tam;
    P->v    = (int*) malloc( P->tam * sizeof(int));
}

int vazia_pilha(pilha * P)
{
    if (P->topo == -1)
        return 1;
    else
        return 0;
}


int cheia_pilha(pilha * P)
{
    if (P->topo == P->tam-1)
        return 1;
    else
        return 0;
}


void imprime_pilha(pilha * P)
{
    for (int i=P->topo; i>=0; i--)
        if (i==P->topo)
            printf("| %2d | <- topo\n", P->v[i]);
        else
            printf("| %2d |\n", P->v[i]);
    printf("\n");
}


void push_pilha(pilha * P, int el)
{
    if (P->topo < P->tam-1)
    {
        P->topo++;
        P->v[P->topo] = el;
    }
    else
        printf("pilha cheia\n");

}


int pop_pilha(pilha * P)
{
    int el;

    if (P->topo >= 0)
    {
        el = P->v[P->topo];
        P->topo--;
    }
    else
        printf("pilha vazia\n");

    return el;
}


int top_pilha(pilha * P)
{
    int el;

    if (P->topo >= 0)
        el = P->v[P->topo];
    else
        printf("pilha vazia\n");

    return el;
}

/******************************* Filas Encadeadas **************************************************/

// Definição do TAD para filas encadeadas

struct NO
{
	int info;
	struct NO *prox;
};
typedef struct NO no;


struct FILA
{
	struct NO *ini;
	struct NO *fim;
};
typedef struct FILA fila;


no * aloca_no(void)
{
    no *aux;
    aux       = (no *) malloc (sizeof(no));
    aux->prox = NULL;

    return aux;
}


fila * aloca_fila(void)
{
    fila *aux;
    aux       = (fila *) malloc (sizeof(fila));
    aux->ini  = NULL;
    aux->fim  = NULL;

    return aux;
}


int vazia_fila(fila * F)
{
    if (F->ini==NULL)
        return 1;
    else
        return 0;
}

void entra_fila(fila *F, int el)
{
    no *p;
    p        = aloca_no();
    p->info  = el;

    if (vazia_fila(F) == 1)
    {
        F->ini = p;
        F->fim = p;
    }
    else
    {
        F->fim->prox = p;
        F->fim       = p;
    }
}


int sai_fila(fila *F)
{
    int el;
    no  *p;

    if (vazia_fila(F) == 1)
    {
        printf("fila vazia\n");
        return -1;
    }
    else
    {
        el     = F->ini->info;
        p      = F->ini;
        F->ini = F->ini->prox;
        free(p);
        return el;
    }
}


int primeiro_fila(fila *F)
{
    if (vazia_fila(F) == 1)
    {
        printf("fila vazia\n");
        return -1;
    }
    else
        return  F->ini->info;
}

void imprime_fila(fila * F)
{
    no* p = F->ini;

    while (p != NULL)
    {
        printf("| %2d |",p->info);
        p = p->prox;
    }
    printf("\n");
}


fila * exclui_fila (fila* F)
{
    no* p = F->ini;
    while (p != NULL)
    {
        no* temp = p->prox;
        free(p);
        p        = temp;
    }
    free(F);

    return NULL;
}




