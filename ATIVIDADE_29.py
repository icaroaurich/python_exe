#29 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vlcdd = int(input("Tu passou a quanto???"))
if vlcdd > 80:
    conta = vlcdd - 80
    mult = float(conta * 7.00)
    print("💰"*50)
    print("Meu patrão, vc passou a {}Km/h, isso da um excesso de {}km/h. Isso vai ficar R${}.".format(vlcdd,conta,mult))
    print("Debito, Crédito ou Dinheiro????")
    print("💰"*50)
else:
    print("👍" * 50)
    print("Diriga com segurança meu patrão 👍👍👍😄😎😙🙃😬")
    print("👍" * 50)