#30 - Crie um programa que leia um número inteiro e mostre na tela se é par ou impar;
numero = int(input("DIGITA AEW: "))
x = numero%2
if x == 0:
    print("é par")
else:
    print("é impar")