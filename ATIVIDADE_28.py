#28 - Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça ao usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário acertou ou não.
import random
rodando = True
while (rodando is True):
    print("#" * 25)
    print("Vou pegar um número entre 1 e 5, tente adivinhar")
    print("#" * 25)
    numeros = [1,2,3,4,5]
    x = random.choice(numeros)
    jogador = int(input("Digite um número entre 1 e 5: "))
    if jogador == x:
        print("Parabéns meu patrão, você acertou")
    else:
        print("Malz aew, eu pensei no {}".format(x))
    y = input("Jogar novamente?")
    if y == "s":
        rodando = True
    else:
        rodando = False