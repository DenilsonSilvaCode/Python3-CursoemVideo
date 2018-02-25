import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #math.ceil (arredonda o numero pra cima)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) #math.ceil (arredonda o numero pra baixo)
