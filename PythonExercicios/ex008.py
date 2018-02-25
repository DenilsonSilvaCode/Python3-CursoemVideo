#leia um valor em metros e converta para centimetros e milimetros

m = float(input('Quantos metros você quer fazer a conversão?: '))
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(m, cm, mm))