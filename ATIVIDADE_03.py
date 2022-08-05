#03 - Crie um programa que leia dois números e mostre a soma entre eles;
pnumero = 10
snumero = 20
print( pnumero + snumero)

## com input precisamos informar que o valor a ser recebido é um número, se não ele só vai juntar um texto no outro.
frase1 = input("Digite o primeiro número: ")
frase2 = input("Digite o segundo número: ")
print(frase1 + frase2)

## forma correta
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
print(numero_1 + numero_2)