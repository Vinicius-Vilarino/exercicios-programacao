n = int(input('Digite um número inteiro: '))
print('1 para binário\n2 para octal\n3 para hexadecimal')
base = int(input('Escolha qual será a base de conversão:'))
if base == 1:
    print('O número {} na base binária é {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('O número {} na base octal é {}'.format(n,oct(n)[2:]))
elif base == 3:
    print('O número {} na base hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
