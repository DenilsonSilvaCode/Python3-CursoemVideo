soma = 0
for c in range(1, 5):
    nota = float(input('Nota do {}º Bimestre: '.format(c)))
    soma = soma + nota
    media = soma / 4
print('sua nota final foi {}'.format(media))
