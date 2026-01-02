#include <stdio.h>

int main() {
    int senha, confirmacao;
    int tentativas = 0;

    printf("Crie uma senha numerica de 4 digitos (nao pode comecar com 0): ");
    scanf("%d", &senha);

    // Verifica se a senha tem 4 dígitos e não começa com 0
    if (senha < 1000 || senha > 9999) {
        printf("Senha invalida! A senha deve ter exatamente 4 digitos e nao pode comecar com 0.\n");
        return 0;
    }

    // Estrutura de repetição para confirmação
    do {
        printf("Confirme sua senha: ");
        scanf("%d", &confirmacao);

        if (confirmacao == senha) {
            printf("Senha confirmada com sucesso!\n");
            return 0;
        } else {
            tentativas++;
            if (tentativas < 3) {
                printf("Senha incorreta! Tentativas restantes: %d\n", 3 - tentativas);
            }
        }

    } while (tentativas < 3);

    printf("Voce errou as tres tentativas possiveis. Programa encerrado.\n");

    return 0;
}
