n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2 #divisão inteira
e = n1**n2 #Potenciação ou expoente
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end='>>>')
print('Divisão inteira {} e potência {}'.format(di, e))


#end=' ' <---- função que determina que a linha ira não sera quebrada;
#\n      <---- quebra de linha;
#{:.2f}  <---- função que determina que dentro dessa caixa o resultado só terá 2 casas decimais (flutuantes/FLOAT)
