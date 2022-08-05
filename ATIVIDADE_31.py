#31- desenvolva um programa que pergunte a pergunte a distancia de uma viagem em Km.
# calcule o preço da passagem, cobrando RS 0,50 por Km para viagens de até 200Km e RS 0,45 para viagens mais longas mais longas.
distancia = int(input("Qual distancia tu vai percorrer?: "))
if distancia <=200:valor = distancia * 0.5
else:valor  = distancia *0.45
print("BORA LÁ, ME PAGUE R${:.2f}".format(valor))