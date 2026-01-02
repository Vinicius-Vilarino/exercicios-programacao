#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main(){
	setlocale(LC_ALL, "Portuguese");

    float nota1, nota2, nota3, nota4, media, nota_final;
    
    printf("Digite a primeira nota: \n");
    scanf("%f", &nota1);
    printf("Digite a segunda nota: \n");
    scanf("%f", &nota2);
    printf("Digite a terceira nota: \n");
    scanf("%f", &nota3);
    printf("Digite a quarta nota: \n");
    scanf("%f", &nota4);
    
    media = (nota1 + nota2 + nota3 + nota4) / 4;
    
    if (media >= 6)
    {
        printf("APROVADO! Com uma média de %.2f \n", media);
    }
    else 
    {
        printf("EXAME FINAL!\n");
        nota_final = 10 - media;
        printf("Você precisa tirar %.2f no exame final para passar.\n", nota_final);
    }
    return 0;
}
