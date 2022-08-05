#12 - Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preço_original = float(input("Qual o preço do produto?: "))
porcentagem = preço_original/100
desconto = porcentagem*5
resultado = preço_original - desconto
print("De acordo meus calculos, se o preço original é {}, com desconto de 5%, seu novo preço será {}".format(preço_original,resultado))