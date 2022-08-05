#13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_original = float(input("Salário: "))
porcentagem = salario_original/100
porcento = porcentagem*15
novo_salario = salario_original+porcento
print("Sendo seu salário anterior {}, seu novo salário com o ajuste de 15 por cento será de {}".format(salario_original,novo_salario))