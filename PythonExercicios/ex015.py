#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado Aluguel de Carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
diaria = (dias * 60) + (km * 0.15)
print('O valor total a pagar foi R${:.2f}'.format(diaria))


