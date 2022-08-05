#14- Escreva um programa que converta uma temperatura digitada em C° e converta para F°;
celsius = float(input("Quantos graus celsius tá aí?: (apenas números)"))
convert = celsius*1.8+32
print("Hum, {} °C equivale a {} °F".format(celsius,convert))