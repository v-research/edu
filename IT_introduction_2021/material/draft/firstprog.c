#include <stdio.h>

int main() {
	int i;
	int input;
	
	scanf("%d", &input);
	for(i=0; i < 10; i++) {			// loop 10 times
		//puts("Hello, world!\n");	// put the string to the output
		printf("Hello, world!\n");
	}
	printf("Input: %d\n", input);
	return 0;						// tell OS the program exited without error
}
