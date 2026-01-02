#include <stdio.h>

float soma(float a, float b);
float subtracao(float a, float b);
float multiplicacao(float a, float b);
float divisao(float a, float b);

void exibirMenu() {
    printf("\n===== CALCULADORA =====\n");
    printf("1 - Soma\n");
    printf("2 - Subtracao\n");
    printf("3 - Multiplicacao\n");
    printf("4 - Divisao\n");
    printf("0 - Sair\n");
    printf("========================\n");
    printf("Escolha uma opcao: ");
}

int main() {
    int opcao;
    float num1, num2, resultado;

    do {
        exibirMenu();
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite dois numeros: ");
                scanf("%f %f", &num1, &num2);
                resultado = soma(num1, num2);
                printf("Resultado: %.2f\n", resultado);
                break;
            case 2:
                printf("Digite dois numeros: ");
                scanf("%f %f", &num1, &num2);
                resultado = subtracao(num1, num2);
                printf("Resultado: %.2f\n", resultado);
                break;
            case 3:
                printf("Digite dois numeros: ");
                scanf("%f %f", &num1, &num2);
                resultado = multiplicacao(num1, num2);
                printf("Resultado: %.2f\n", resultado);
                break;
            case 4:
                printf("Digite dois numeros: ");
                scanf("%f %f", &num1, &num2);
                if (num2 == 0) {
                    printf("Erro! Divisao por zero nao permitida.\n");
                } else {
                    resultado = divisao(num1, num2);
                    printf("Resultado: %.2f\n", resultado);
                }
                break;
            case 0:
                printf("Encerrando o programa...\n");
                break;
            default:
                printf("Opcao invalida! Tente novamente.\n");
        }

    } while (opcao != 0);

    return 0;
}

float soma(float a, float b) {
    return a + b;
}

float subtracao(float a, float b) {
    return a - b;
}

float multiplicacao(float a, float b) {
    return a * b;
}

float divisao(float a, float b) {
    return a / b;
}
