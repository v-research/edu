#include <stdio.h>

int main() {
	int a, b;
	float c, d;
	a = 13;
	b = 5;
	c = a / b;
	d = (float) a / (float) b; 
	// Divide using integers. 
	// Divide integers typecast as floats.
	printf("[integers]\t a = %d\t b = %d\n", a, b);
	printf("[floats]\t c = %f\t d = %f\n", c, d);
}