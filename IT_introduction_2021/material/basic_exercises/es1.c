#include <stdio.h>

int main() {
	// Ripassiamo gli array
	int a[] = {1, 2, 3};
	char b[10];
	char s[10];
	
	s[0] = 'a';
	s[1] = '\0';
	s[2] = 'b';
	b[10] = '\0';
	
	printf("%s\n", s);
	printf("%s\n", b);
	
	return 0;
}