'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
nome1 = input('Primeiro Aluno: ')
nome2 = input('Segundo Aluno: ')
nome3 = input('Terceiro Aluno: ')
nome4 = input('Quarto Aluno: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A Ordem de Apresentação será ')
print(lista)