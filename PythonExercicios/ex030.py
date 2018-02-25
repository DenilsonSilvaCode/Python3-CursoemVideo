'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n = int(input('Me diga um numero qualquer: '))
resultado = n % 2
if resultado == 0:
    print('Este numero é PAR')
else:
    print('Este numero é IMPAR')