#include <stdio.h>

int varGlobale = 5;

void stampa(char s[]) {
	int i;
	
	for (i=0; s[i]!='\0'; i++) {
		printf("%c", s[i]);
	}
	printf("\n");
	
	printf("%d\n", varGlobale);
}

int main() {
	//int i;
	char s1[] = {'c', 'i', 'a', 'o', '\0'};
	char s2[] = {'L', 'u', 'c', 'a', '\0'};
	char s3[] = {'G', 'i', 'g', 'i', '\0'};	
	
	stampa(s1);
	varGlobale++;
	printf("%d\n", varGlobale);
	stampa(s2);
	varGlobale++;
	printf("%d\n", varGlobale);
	stampa(s3);
	
	/*for (i=0, s1[i]!='\0'; i++) {
		printf("%c");
	}
	printf("\n");
	for (i=0, s2[i]!='\0'; i++) {
		printf("%c");
	}
	printf("\n");
	for (i=0, s3[i]!='\0'; i++) {
		printf("%c");
	}
	printf("\n");*/
	
	return 0;
}