#19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
# sortear = aleatório
import random
n1 = "Icaro"
n2 = "Raul"
n3 = "Allan"
n4 = "Pam"
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(escolhido)