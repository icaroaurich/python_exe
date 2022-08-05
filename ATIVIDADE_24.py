#24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo";
cidade_original = "Santo eunapolis"
cidade = cidade_original.lower()
x = cidade_original.find("santo")
print(x)
if x == 0:
    print("Tem Santo no começo")
elif x != -1 and x!= 0:
    print("Tem Santo mas não é no começo")
else:
    print("Não tem santo")