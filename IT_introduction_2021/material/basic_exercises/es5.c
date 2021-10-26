#include <stdio.h>

int main() {
	int i;
	char s[] = {'c', 'i', 'a', 'o', '\0'};
	char *p = s;
	
	for (i=0; *(p+i)!='\0'; i++) {
		printf("%c\n\n", *(p+i));
	}
	printf("\n");
	
	return 0;
}
