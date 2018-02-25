'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

'''=================UTILIZANDO FOR====================
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #divide a frase em grupos
junto = ''.join(palavras) #juntou as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso ==junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é palíndromo!')================='''

'''=============UTILIZANDO FATIAMENTO=================='''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #divide a frase em grupos
junto = ''.join(palavras) #juntou as palavras
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso ==junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é palíndromo!')
