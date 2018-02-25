'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. '''

while True:
    n = int(input('Quer ver a tabuada de que valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {n * c:2}')
    print('-' * 30)
    print('Digite um Valor negativo para encerrar(ex:-5)')
    print('-' * 30)
print('PROGRAMA TADUADA ENCERRADA')
