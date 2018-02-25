# %% -------------- DESAFIO 71 -----------------
print('------------- CAIXA DA GALERA -------------')
while True:
    print('==================================')
    escolha = '0'
    valor = int(input('Qual valor deseja sacar? R$ '))
    c50 = valor // 50
    c20 = (valor - c50 * 50) // 20
    c10 = (valor - c50 * 50 - c20 * 20) // 10
    c5 = (valor - c50 * 50 - c20 * 20 - c10 * 10) // 5
    c2 = (valor - c50 * 50 - c20 * 20 - c10 * 10 - c5 * 5) // 2
    c1 = c5 = (valor - c50 * 50 - c20 * 20 - c10 * 10 - c5 * 5 - c2 * 2)

    if c50 != 0:
        print(f'Total de {c50} cedulas de R$ 50')
    if c20 != 0:
        print(f'Total de {c20} cedulas de R$ 20')
    if c10 != 0:
        print(f'Total de {c10} cedulas de R$ 10')
    if c5 != 0:
        print(f'Total de {c5} cedulas de R$ 5')
    if c2 != 0:
        print(f'Total de {c2} cedulas de R$ 2')
    if c1 != 0:
        print(f'Total de {c1} cedulas de R$ 1')

    while escolha != 'S' and escolha != 'N':
        escolha = input('Deseja continuar? [S/N]').upper()
    if escolha == 'N':
        break
    print('==================================')
print('--------------------- ENCERRADO ------------------')