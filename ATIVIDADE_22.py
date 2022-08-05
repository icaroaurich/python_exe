#22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras Maiúsculas e Minúsculas
# Quantas letras ao todo (sem considerar espaço)
#  Quantas letras tem o primeiro nome.
            import time
            nome = "icaro aurich"
            upp = nome.upper()
            low = nome.lower()
            cont = len(nome) - (nome.count(' '))
            new = nome.find(' ')
            print(nome,"\n","ANALISANDO...")
            time.sleep(3)
            print(upp,"\n",low,"\n",cont,"\n",new)