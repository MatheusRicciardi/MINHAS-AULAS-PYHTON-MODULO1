#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua area e a quantidade de tinta necessaira para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m quadrados

altura = float(input('Determine a altura de sua parede:'))
largura = float(input('Determine a largura de sua parede:'))

area = altura * largura
area_quadrada = area ** 2
print('A sua parede tem {} de area'.format(area))
print('E {} de area quadrada'.format(area_quadrada))