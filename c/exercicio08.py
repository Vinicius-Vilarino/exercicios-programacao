#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main(){
	setlocale(LC_ALL, "Portuguese");

    int num1, num2;
    
    printf("Digite o primeiro número: \n");
    scanf("%d", &num1);
    printf("Digite o segundo número: \n");
    scanf("%d", &num2);
    
    if (num1 == num2)
    {
        printf("Os números são iguais\n");
    }
    else
    {
        if (num1 > num2)
        {
            printf("O primeiro número é maior que o segundo.\n");
        }
        else 
        {
            printf("O segundo número é maior que o primeiro.\n");
        }
        return 0;
    }
}
