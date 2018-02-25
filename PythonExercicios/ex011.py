#faça um programa que leia a altura e largura de uma parede em metros, calcule a sua area, e a quantidade de tinta necessária para pinta-la.
#sabendo que cada litro de tinta pinta uma area de 2m²

larg = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = larg * alt
print('Sua parede tem {}m²'.format(area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {} Litros de tinta.'.format(tinta))

