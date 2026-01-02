soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
print('A soma dos números ímpares divisíveis por 3 entre 1 e 500 é: {}'.format(soma))
