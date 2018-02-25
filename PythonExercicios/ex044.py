'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('========== LOJAS GUANABARA ==========')
preço = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? ' ))
if opcao == 1:
    desconto = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preço, desconto))
elif opcao == 2:
    desconto = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preço, desconto))
elif opcao == 3:
    parcelamento = preço / 2
    print('Sua compra de R${:.2f} vai custar 2x de R${:.2f}.'.format(preço, parcelamento))
elif opcao == 4:
    parcelas = int(input('quantas parcelas? '))
    juros = preço + (preço * 20 / 100)
    parcelamento = juros / parcelas
    print('Sua compra será parcelada em {}x de R${} COM JUROS.'.format(parcelas, parcelamento))
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preço, juros))
else:
    print('Opção invalida.')