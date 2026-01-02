from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
if idade < 18:
    saldo = 18 - idade
    print('Ele ainda vai se alistar no serviço militar. Faltam {} anos para o alistamento.'.format(saldo))
elif idade == 18:
    print('Está na hora de se alistar.')
elif idade > 18:
    saldo = idade - 18
    print('Já passou da hora de se alistar. Seu alistamento foi a {} anos.'.format(saldo))
