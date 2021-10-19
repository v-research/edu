#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

enum colore{Bianco, Nero};

typedef enum colore tcolore;

void leggi_vettore(int v[], int dim) {
    int i;
    for (i=0; i<dim; i++)
        scanf("%d", &v[i]);
}

/*int abcd = 0;*/

void rimuoviElemento(int v[], int dim) {
    int i;

    for (i=0; i<dim; i++) {
        v[i] = v[i+1];
    }
}

int grattacielo(int reward[100], tcolore colore, int n) {
    // completare
}

int main() {
    int reward[100];
    int n;
    scanf("%d", &n);
    leggi_vettore(reward, n);
    printf("%d", grattacielo(reward, Bianco, n));
    return 0;
}
