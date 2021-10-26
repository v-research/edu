#include <stdio.h>
#include <stdbool.h>

bool nPrimo(int n) {
    bool primo = true;

    if (n == 2) {
        return primo;
    }
    else {
        int i = 2;

        while (i < n && primo) {
            if (n%i == 0) {
                primo = false;
            }

            i++;
        }

        return primo;
    }
}

int main() {
    int n;
    bool primo;

    printf("Inserisci un numero e vediamo se e' primo: ");
    do {
        scanf("%d", &n);
    } while (n <= 0);

    primo = nPrimo(n);

    if (primo) {
        printf("%d e' un numero primo\n", n);
    }
    else {
        printf("%d non e' un numero primo\n", n);
    }

    return 0;
}