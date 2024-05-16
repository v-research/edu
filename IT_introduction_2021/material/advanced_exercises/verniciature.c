#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

enum colore{Bianco, Nero};

typedef enum colore tcolore;

void leggi_vettore(int v[], int dim)
{
    int i;
    for (i=0; i<dim; i++)
        scanf("%d", &v[i]);
}

/*int abcd = 0;*/

void rimuoviElemento(int v[], int dim) {

    int i;

    /*if (abcd == 0) {
        for (i=0; i<dim; i++) {
            printf("%d ", v[i]);
        }
        printf("\nDimensione: %d\n", dim);
        abcd++;
    }*/

    for (i=0; i<dim; i++) {
        v[i] = v[i+1];
    }
}

int grattacielo(int reward[100], tcolore colore, int n) {
    if (n == 0) {
        return 0;
    }
    else {
        if (colore == Bianco) {
            /*printf("Bianco");*/
            if (n == 1) {
                return reward[0];
            }
            else {
                int guadagno = 0;
                if (reward[0] >= reward[1]) {
                    guadagno = reward[0];
                    rimuoviElemento(reward, n);
                    /*printf("%d ", guadagno);*/
                    return guadagno + grattacielo(reward, Nero, n-1);
                }
                else if (n > 4 && reward[0] < reward[1] && reward[1] < reward[2] && reward[2] < reward[3]) {
                    guadagno = reward[1];
                    rimuoviElemento(reward, n);
                    /*printf("%d ", guadagno);*/
                    return guadagno + grattacielo(reward, Nero, n-1);
                }
                else if (n > 3 && reward[0] < reward[1] && reward[1] < reward[2]) {
                    guadagno = reward[0];
                    rimuoviElemento(reward, n);
                    /*printf("%d ", guadagno);*/
                    return guadagno + grattacielo(reward, Nero, n-1);
                }
                else {
                    rimuoviElemento(reward, n);
                    return grattacielo(reward, Bianco, n-1);
                }
            }
        }
        else {
            /*printf("Nero");*/
            rimuoviElemento(reward, n);
            return grattacielo(reward, Bianco, n-1);
        }
    }
}

int main() {
    int reward[100];
    int n;
    scanf("%d", &n);
    leggi_vettore(reward, n);
    printf("%d", grattacielo(reward, Bianco, n));
    return 0;
}
