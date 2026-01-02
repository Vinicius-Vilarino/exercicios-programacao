import random
num_computador = [0, 1, 2, 3, 4, 5]
num_usuario = int(input('Digite um número de 0 a 5: '))
escolha_computador = random.choice(num_computador)
if num_usuario == escolha_computador:
    print('Parabéns! Você pensou no número {}, o mesmo que o meu!'.format(num_usuario))
else:
    print('Você errou! Eu estava pensando no número {}.'.format(escolha_computador))
