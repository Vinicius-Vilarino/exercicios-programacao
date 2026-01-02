#include <stdio.h>

int main(){
	int A, B, C, D;
	
	printf("Digite o valor de A: ");
	scanf("%d", &A);
	printf("Digite o valor de B: ");
	scanf("%d", &B);
	printf("Digite o valor de C: ");
	scanf("%d", &C);
	printf("Digite o valor de D: ");
	scanf("%d", &D);
	
	printf("MULTIPLICAÇÕES: \n");
	printf("A x B = %d\n", A * B);
	printf("A x C = %d\n", A * C);
	printf("A x D = %d\n", A * D);
	printf("B x C = %d\n", B * C);
	printf("B x D = %d\n", B * D);
	printf("C x D = %d\n", C * D);
	
	printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
	
	printf("ADIÇÕES: \n");
	printf("A + B = %d\n", A + B);
	printf("A + C = %d\n", A + C);
	printf("A + D = %d\n", A + D);
	printf("B + C = %d\n", B + C);
	printf("B + D = %d\n", B + D);
	printf("C + D = %d\n", C + D);
	return 0;
}
