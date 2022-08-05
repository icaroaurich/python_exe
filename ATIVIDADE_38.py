#38- escreva um programa que leia dois numeros e compare-os.
# -o primeiro valor é maior -o segundo valor é maior -não existe valor maior, os dois sao iguais.
rodando = True
while (rodando is True):
    numero_1 = int(input("DIGITA o primero: "))
    numero_2 = int(input("DIGITA o segundo: "))
    if numero_1 > numero_2:print("O primeiro número é  maior")
    elif numero_2 > numero_1:print("O segundo número é  maior")
    else:print("Eles são iguais")