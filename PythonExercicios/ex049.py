'''Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Escreva um Número: '))
print('Veja a baixo a tabuada do Número digitado')
print('-'*12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-'*12)
