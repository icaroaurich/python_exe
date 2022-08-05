#20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e motre a ordem sorteada.
# boar
import random
n1 = "Icaro"
n2 = "Raul"
n3 = "Allan"
n4 = "Pamela"
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A ordem será")
print(lista)