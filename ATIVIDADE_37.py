#37- Escreva um programa que leia um numero inteiro qualquer a peça para o usuario escolher qual será a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal
# 5000 = 1001110001000
import time
rodando = True
while (rodando is True):
    print("#"*20)
    print("Seja bem vindo ao conversor de números para outros números (nome criativo, eu sei)")
    numero = int(input("Primeiro, digite seu número: "))
    print("converter para oq? ")
    print("### BINÁRIO..................1 ")
    print("### OCTAL.......................2 ")
    print("### HEXADECIMAL......3 ")
    operador = input("Operador: ")
    print("Okay, o número será: ",numero)
    lista = []
    print("Aguarde...")
    time.sleep(1)
    if operador == "1":
        for x in range(10000):
            resto = numero%2
            lista.append(resto)
            numero = int(numero /2)
            #print("Resto: ", resto)
            if numero == 1:
                lista.append(numero)
                break
    elif operador == "2":
        for x in range(10000):
            resto = numero % 8
            lista.append(resto)
            numero = int(numero / 8)
            # print("Resto: ", resto)
            if numero == 1:
                lista.append(numero)
                break
    elif operador == "3":
        for x in range(10000):
            if numero < 16:
                if numero == 0:lista.append(0)
                elif numero == 1:lista.append(1)
                elif numero == 2:lista.append(2)
                elif numero == 3:lista.append(3)
                elif numero == 4:lista.append(4)
                elif numero == 5:lista.append(5)
                elif numero == 6:lista.append(6)
                elif numero == 7:lista.append(7)
                elif numero == 8:lista.append(8)
                elif numero == 9:lista.append(9)
                elif numero == 10: lista.append("A")
                elif numero == 11:lista.append("B")
                elif numero == 12:lista.append("C")
                elif numero == 13:lista.append("D")
                elif numero == 14:lista.append("E")
                elif numero == 15:lista.append("F")
                elif numero == 16:lista.append("G")
                break
            resto = numero % 16
            if resto == 10:lista.append("A")
            elif resto == 11:lista.append("B")
            elif resto == 12:lista.append("C")
            elif resto == 13:lista.append("D")
            elif resto == 14:lista.append("E")
            elif resto == 15:lista.append("F")
            elif resto == 16:lista.append("G")
            else:lista.append(resto)
            numero = int(numero / 16)
            # print("Resto: ", resto)
            if numero == 1:
                lista.append(numero)
                break
    final = lista[::-1]
    #final.reverse()
    print("Seu número em  é: ",final)
    y = input("Outro número? (s/n)  ")
    if y == "s":rodando = True
    elif y == "n":
        print("Então vai catar coquinho")
        break
    else:break