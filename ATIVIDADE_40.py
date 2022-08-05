#30 Crie um programa que leia duas notas de um aluno e calcule sua média atingida:
# Média abaixo de 5.0:REPROVADO -Média entre 5.0 e 6.9:RECUPERAÇÃO -Média 7.0 ou superior:APROVADO
nota_1 = int(input("Digite sua primeira nota (0-100): "))
nota_2 = int(input("Digite sua segunda nota (0-100): "))
media = int((nota_1 + nota_2) / 2)
print(media)
if media < 50: print("REPROVADO")
elif media >50 and media <69:
    for nota in range(100 - media):
        print("ESTUDE MAIS")
elif media > 70:print("Passou meu brother")
