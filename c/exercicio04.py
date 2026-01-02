#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	
    int valor;
    
    printf("Digite um número de 1 a 4 \n");
    scanf("%d", &valor);
    
    switch(valor)
    {
        case 1:
            printf("Primavera\n");
            break;
            
        case 2:
            printf("Verão\n");
            break;
        
        case 3:
            printf("Outono\n");
            break;
        
        case 4:
            printf("Inverno\n");
            break;
            
        default:
            printf("Opção inválida\n");
            break;
    }
    
    return 0;
}
