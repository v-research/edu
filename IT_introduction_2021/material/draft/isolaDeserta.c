#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void printInput(int disponibilita[], int peso[], int utilita[], int dim, int avanzo) {
	// consigliato per debugging
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
    // completare
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
