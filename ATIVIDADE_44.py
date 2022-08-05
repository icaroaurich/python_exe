# 44 - Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e a condição de pagamento:
# á vista dinheiro/cheque:10% de desconto
# á vista no cartão:5% de desconto
# em até 2x no Cartão preço normal
# 3x ou mais no cartçao:20% de juros
rodando_master = True
while rodando_master is True:
    rodando = True
    while rodando is True:
        pro_pre = float(input("Preço do produto: "))
        pro_qua = float(input("Quantidade do produto: "))
        pro_val = pro_pre*pro_qua
        rodando2 = True
        while rodando2 is True:
            print("🎇"*50)
            print("Valor do orçamento: R${:.2f}".format(pro_val))
            print("Formas de pagamento disponíveis:")
            print("-" * 50)
            print("1 - Á vista dinheiro / Cheque......Desconto de 10%")
            print("2 - Á vista Cartão................................Desconto de 05%")
            print("3 - Em até 2x no cartão...................Preço Normal")
            print("4 - 3x ou mais no cartão.................20% Juros")
            print("-" * 50)
            pro_pag = input("Por favor, selecione uma forma de pagamento disponível: ")
            print("Forma de pagamento selecionada: {}".format(pro_pag))
            if pro_pag != "1" and pro_pag != "2" and pro_pag != "3" and pro_pag != "4":
                print("Forma de pagamento selecionada é INVÁLIDA.")
                print("Por favor, selecione uma forma de pagamento VÁLIDA.")
            else:
                rodando3 = True
                while rodando3 is True:
                    proceguir = input("Deseja continuar? (s/n): ")
                    proceguir = proceguir.lower()
                    if proceguir != "s" and proceguir != "n":
                        print("Conteudo informado é inválido, por favor, digite [s] ou [n].")
                    elif proceguir == "s":
                        if pro_pag == "1":
                            preco_final = pro_val * 0.90
                            print("O preço a ser pago será: {:.2f}".format(preco_final))
                            rodando3 = False
                            rodando2 = False
                            rodando1 = False
                            rodando = False
                        elif pro_pag == "2":
                            preco_final = pro_val * 0.95
                            print("O preço a ser pago será: {:.2f}".format(preco_final))
                            rodando3 = False
                            rodando2 = False
                            rodando1 = False
                            rodando = False
                        elif pro_pag == "3":
                            preco_final = pro_val * 1
                            print("O preço a ser pago será: {:.2f}".format(preco_final))
                            rodando3 = False
                            rodando2 = False
                            rodando1 = False
                            rodando = False
                        elif pro_pag == "4":
                            preco_final = pro_val * 1.20
                            print("O preço a ser pago será: {:.2f}".format(preco_final))
                            rodando3 = False
                            rodando2 = False
                            rodando1 = False
                            rodando = False
                    elif proceguir == "n":
                        rodando3 = False
    rodando_final = True
    while rodando_final is True:
        novamente = input("Quer realizar outro orçamento? (s/n)")
        novamente = novamente.lower()
        if novamente != "s" and novamente != "n":
            print("Conteudo informado é inválido, por favor, digite [s] ou [n].")
        elif novamente == "s":
            rodando_final = False
        elif novamente == "n":
            rodando_final = False
            rodando_master = False
            break
