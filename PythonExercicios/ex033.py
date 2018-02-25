'''Faça um programa que leia três números
e mostre qual é o maior e qual é o menor.'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Segundo Valor: '))
#verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Menor valor foi {}'. format(menor))
print('Maior valor foi {}'.format(maior))
