#include <stdio.h>
#include <stdlib.h>

int main(){
	int w;
		for (w = 1; w <= 15; w++)
		{
			if (w == 8)
			{
				break;
			}
			printf("%d\n", w);
		}
		printf("\n \n Parar a condicao de repeticao w = %d \n", w);
	return 0;         
}
