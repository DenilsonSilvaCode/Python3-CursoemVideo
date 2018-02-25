'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = float(input('Qual a velocidade atual do carro? Km/h '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma Multa de R${:.2f}!'.format(multa))
else:
    print('OK, Você está na velocidade que a via permite, \nFaça uma ótima viagem!')
