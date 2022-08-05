#25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome;
nome = "joao silva da SilVa"
a = nome.lower()
b = a.find("silva")
print(b)
if b == -1:
    print("Não tem Silva")
else:
    print("Tem Silva")