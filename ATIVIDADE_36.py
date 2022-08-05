#36- escrema um programa para aprovar o emprestimo bancario para a compra de uma casa.
# pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, nao pode exeder 30% do salario ou então o emprestimo será negado.
valor = 20000
salario = 1200
tempo = 60 #meses
#valor / tempo !> 30% in salario
pagar_mensal = valor / tempo
print("Seguinte, tu vai ter me pagar: ",pagar_mensal)
print("30% do teu salario é:",salario*0.30)
if pagar_mensal > salario*0.30:print("Desculpe amigo, mas vc não pode comprar isso...")
else:print("Segue firme")
