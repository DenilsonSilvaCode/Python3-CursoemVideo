'''Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade ,atual))

print('''Qual o seu sexo? 
[1] Masculino
[2] Feminino''')
opcao = int(input('Digite aqui: '))
if opcao == 2:
    print('Você é Mulher, para você o Alistamento Militar não é OBRIGATÓRIO no Brasil!')
if opcao == 1 and idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE')
elif opcao == 1 and idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif opcao == 1 and idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado já {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))



