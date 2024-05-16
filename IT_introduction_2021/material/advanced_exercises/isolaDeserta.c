#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


int print = 0;
void printInput(int disponibilita[], int peso[], int utilita[], int dim, int avanzo) {
    int i = 0;
    printf("disponibilita': ");
    for (i=0; i<dim; i++) {
        printf("%d ", disponibilita[i]);
    }
    printf("\n");
    printf("peso: ");
    for (i=0; i<dim; i++) {
        printf("%d ", peso[i]);
    }
    printf("\n");
    printf("utilita': ");
    for (i=0; i<dim; i++) {
        printf("%d ", utilita[i]);
    }
    printf("\navanzo: %d\n", avanzo);

}

void cpArray(int *v1, int *v2, int dim) {
    int i = 0;
    for (i=0; i<dim; i++) {
        v1[i] = v2[i];
    }
}

int max(int a, int b) {
    if (a>b) {
        return a;
    }
    else {
        return b;
    }
}

int isoladeserta(int disponibilita[], int peso[], int utilita[], int dim, int avanzo) {
    print++;
    if (print==0) {
        printInput(disponibilita, peso, utilita, dim, avanzo);
        print++;
    }

    int maxU = 0;
    int *dispAux = malloc(sizeof(int)*(dim));
    cpArray(dispAux, disponibilita, dim);

    if (dim == 0 || avanzo == 0) {
        return maxU;
    }
    else if (disponibilita[dim-1]==0 || peso[dim-1]>avanzo) {
        return maxU += isoladeserta(disponibilita, peso, utilita, dim-1, avanzo);
    }
    else {
        disponibilita[dim-1]--;
        int lMax = utilita[dim-1]+isoladeserta(disponibilita, peso, utilita, dim, avanzo-peso[dim-1]);
        int rMax = isoladeserta(dispAux, peso, utilita, dim-1, avanzo);
        return maxU += max(rMax, lMax);
    }
}

int main()
{

    int dim; int i;
    int vp[100], vu[100], vd[100];

    scanf("%d", &dim);

    for (i=0; i<dim; i++)
    {
        scanf("%d", vd+i);
        scanf("%d", vp+i);
        scanf("%d", vu+i);
    }

    printf("%d\n", isoladeserta(vd,vp,vu,dim,20));

    return 0;
}
