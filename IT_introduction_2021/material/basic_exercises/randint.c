#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int i, n;
    
    srand(time(NULL));
    n = 10;
    for (i=0; i<5; i++) {
        printf("Numero random: %d\n", rand()%n);
    }

    return 0;
}
