'''Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.'''

from time import sleep
import emoji
print('-='*20)
print('CONTAGEM REGRESSIVA')
print('-='*20)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
for c in range(0, 9):
    print(emoji.emojize('  :fireworks:  '), end='')
print('\n* * * * * * * * * * FELIZ ANO NOVO * * * * * * * * *')
for c in range(0, 9):
    print(emoji.emojize('  :fireworks:  '), end='')