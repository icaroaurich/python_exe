#15 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
print("### 24h equivale a 1 dia, 25h já conta como 2 dias ###")
dias = int(input("Quantos dias você ficou com o carro?: "))
km = float(input("Quantos km foram percorridos?: "))
pagar_dias = dias*60
pagar_km = km*0.15
total = pagar_dias+pagar_km
print("Seguinte, o custo do carro ficou R${} por {} dias, e a kilometragem ficou R${} por {} km. Somando um total de {}".format(pagar_dias,dias,pagar_km,km,total))