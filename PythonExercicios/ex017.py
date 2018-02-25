'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

'''------------USANDO FORMULA MATEMATICA-----------'''
'''catetooposto = float(input('Digite o Cateto Oposto: '))
catetoadjacente = float(input('Digite o Cateto Adjacente: '))
calculo1 = (catetooposto**2) + (catetoadjacente**2)
hipotenusa = calculo1**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

'''---------USANDO MODULOS--------------'''

from math import hypot
catetooposto = float(input('Digite o Cateto Oposto: '))
catetoadjacente = float(input('Digite o Cateto Adjacente: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))