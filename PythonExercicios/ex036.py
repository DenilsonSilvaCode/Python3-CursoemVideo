'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

from time import sleep
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto você ganha mensal? R$ '))
tempo = int(input('Em quantos anos você pretende pagar? '))
parcela = casa / (tempo * 12)
meses = tempo * 12
aprov = salario * 30 / 100

print('Simulando a sua parcela ficará em\n{}x de R${:.2f}'.format(meses, parcela))
print('Verificando aprovação... ')
sleep(5)
if aprov >= parcela:
    print('Seu financiamento foi aprovado! Parabéns')
else:
    print('Seu financiamento foi NEGADO! Procure um avalista ...')

