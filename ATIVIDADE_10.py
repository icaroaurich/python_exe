#10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere U$1,00 = R$5,08
# Considere U$1,00 = R$5,08
print("\n","### Para números quebrados, utilize . (ponto) ###")
carteira = float(input("Me diga aew, quanto tu tem na carteira? (apenas números): "))
dolar = 5.08
convert = carteira / dolar
print("Você tem {} de dolares, kkkk mó pobre".format(convert))