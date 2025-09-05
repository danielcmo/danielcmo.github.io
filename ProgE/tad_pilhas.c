// Definição do TAD para Pilha em vetores

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



