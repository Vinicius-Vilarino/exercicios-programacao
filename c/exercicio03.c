#include <stdio.h>
#include <iso646.h>
int main() {
    int num, resto4, resto5;
    printf("Digite um numero inteiro: ");
    scanf("%d", &num);

    resto4 = num % 4;
    resto5 = num % 5;
    
    if (resto4 == 0 and resto5 == 0)
        printf("O número %d é divisível por 4 e 5.", num);
    else
        printf("Valor não é divisível por 4 e 5!");
      
    return 0;
}
