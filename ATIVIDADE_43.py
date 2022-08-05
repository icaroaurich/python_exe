#43- desenvolva uma logica que leia o peso e a altira de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5:abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40:Obesidade
# Acima de 40: obesidade mórbida
# IMC = peso/ (altura x altura)
rodando = True
while (rodando is True):
    altura = float(input("Qual sua altura em metros? "))
    peso = float(input("Qual o seu peso em kg? "))
    imc = peso/(altura*altura)
    print("Teu IMC é: {:.2f}".format(imc))
    if imc <= 18.5:print("Abaixo do peso")
    elif imc > 18.5 and imc <= 25:print("Peso ideal")
    elif imc > 25 and imc <= 30:print("Sobrepeso")
    elif imc > 30 and imc <= 40:print("Obesidade")
    elif imc > 30:print("Obesidade mórbida")