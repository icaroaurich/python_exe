#27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente. EX: Icaro Santos Aurich
# PRIMEIRO = ICARO // ULTIMO = AURICH
nome = "         icaro aurich      ".strip()
x = nome.split()
print("Primeiro nome = {}".format(x[0]))
print("Ultimo nome = {}".format(x[len(x)-1]))
