#34- Escreva um programa que pergunte o salario de um funcionario e calcule o seu aumento.
# para salarios superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o Aumento é de 15%

salario = float(input("DIGA SEU SALARIO: "))
if salario >= 1250: final = salario * 1.10
else: final = salario*1.15
print(final)