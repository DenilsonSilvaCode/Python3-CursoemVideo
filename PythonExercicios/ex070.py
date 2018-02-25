#leia preços e nome do produto
#pergunte se quer continuar
#total gasto na compra
#quantos produtos custam mais que 1000
#nome do produto mais barato
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1.000'.format(totmil))
print('O produto mais barato custa R${:.2f}'.format(menor))

