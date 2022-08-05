#16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. EX: Número = 6.123 // Inteiro = 6;
receber_float = float(input("Me de um número quebrado: "))
numero_int = int(receber_float)
print("Sua parte inteira ficou {}. (Arredondamento não foi considerado)".format(numero_int))

novo = float(input("ME DA MAIS: "))
coisa = novo // 1
print(coisa)