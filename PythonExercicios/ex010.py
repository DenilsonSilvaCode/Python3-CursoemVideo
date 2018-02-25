#crie um programa que calcule quantos Reais a pessoa tem na carteira e mostre quantos Dolares ela poderia comprar com esse valor;

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
