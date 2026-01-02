num = int(input('Digite um número: '))
print('Tabuada do {}:'.format(num))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, num * i))
