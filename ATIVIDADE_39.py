#30 fala um programa que leia o ano de nacimento de um jovem e iunforme. de acordo com sua idade, se ele ainda vai se alistar ao serviço militar.
# se é a hora de se alistar ou se já passou do tempo do alistamento.
#Seus programa tambem devera mostrar o tempo que falta ou que passou do prazo.
numero = int(input("Você nasceu em que ano? "))
calculo = 2021 - numero
print("Hum, então tu tem {} anos".format(calculo))
atraso = 18 - calculo
if atraso < 0:atraso = atraso * -1
#print(atraso)
faltam = atraso
#print(faltam)
if calculo == 18:print("Você precisa se alistar meu patrão.")
elif calculo >= 19:
    print("Já passou da hora de se alistar meu patrão.")
    if atraso == 1: print("E você está atrasado {} ano.".format(atraso))
    elif atraso > 1: print("E você está atrasado {} anos.".format(atraso))
elif calculo <= 17:
    print("Não precisa de alistar, tá de boa.")
    if faltam == 1:print("Mas falta {} ano.".format(faltam))
    elif faltam >1:print("Mas faltam {} anos.".format(faltam))
