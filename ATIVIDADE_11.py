#11 - Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária paar pintá-la, sabendoq ue cada litro de tinta pinta uma área de 2m²;
#1L = 2²m
alt_parede = float(input("Digite a altura da parede: "))
lar_parede = float(input("Digite a largura da parede: "))
area_da_parede = alt_parede * lar_parede
comprar = area_da_parede/2

print("Amigo, seguindo seus dados, vc vai percisar de {} latas de tinta, aproximadamente.".format(comprar))