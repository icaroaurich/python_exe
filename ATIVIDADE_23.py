#23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados; EX: 1234 Unidade = 4 dezena = 3 centena = 2 milhar = 1
numero = 1234
conta_unidade = numero // 1 % 10
conta_dezena = numero // 10 % 10
conta_centena = numero // 100 % 10
conta_milhar = numero // 1000 % 10
print("##########")
print("Número = ",numero)
print("Unidade = ",conta_unidade)
print("Dezena =  ",conta_dezena)
print("Centena =  ",conta_centena)
print("Milhar =  ",conta_milhar)
#print("primeiro é {}, segundo é {}, terceiro é {}, e o quarto é {}".format(numero[0],numero[1],numero[2],numero[3]))
