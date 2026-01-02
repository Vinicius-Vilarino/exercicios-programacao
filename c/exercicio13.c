#include <stdlib.h>
#include <stdio.h>
#include <string.h> 

int main() {
    system("chcp 65001");

    char nome[30], sobrenome[50];
    float nota[4], media;

    printf("Digite o seu nome: ");
    fflush(stdin);
    fgets(nome, 30, stdin);
    nome[strcspn(nome, "\n")] = '\0'; 

    printf("Digite o seu sobrenome: ");
    fflush(stdin);
    fgets(sobrenome, 50, stdin);
    sobrenome[strcspn(sobrenome, "\n")] = '\0'; 

    printf("Digite a sua primeira nota: ");
    scanf("%f", &nota[0]);
    printf("Digite a sua segunda nota: ");
    scanf("%f", &nota[1]);
    printf("Digite a sua terceira nota: ");
    scanf("%f", &nota[2]);
    printf("Digite a sua quarta nota: ");
    scanf("%f", &nota[3]);

    media = (nota[0] + nota[1] + nota[2] + nota[3]) / 4;

    printf("%s %s, sua nota média na matéria foi de %.2f!\n", nome, sobrenome, media);
    return 0;
}
