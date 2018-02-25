#leia idade e sexo de varias pessoas
# a cada pessoa pergunte se quer continuar S/N?
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

mais18 = 0
homens = 0
mulher20 = 0
resposta = ''
while True:
    print('=-=' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('=-=' * 20)
    resposta = str(input('Deseja continuar com o cadastro? [S/N]')).upper().strip()[0]
    if idade >=18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <=20:
        mulher20 += 1
    if resposta == 'N':
            break
print('~' * 20)
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Dessa lista {mulher20} mulheres tem menos de 20 anos.')
print('~' * 20)
