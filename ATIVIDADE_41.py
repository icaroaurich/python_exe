#41 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM -Até 14 anos:INFANTIL -Até 19 anos:JUNIOR -Até 25 anos:SÊNIOR -Acima:MASTER;
rodando = True
while (rodando is True):
    print("🎇" * 50)
    ano = int(input("Em q ano tu nasceu? "))
    idade = 2021 - ano
    if idade < 0:
        print("C nasceu no futuro?")
    else:
        print(idade)
        if idade >0 and idade <= 9:print("Mirim")
        elif idade >9 and idade <= 14:print("Infantil")
        elif idade >14 and idade <= 19:print("Mirim")
        elif idade >19 and idade <= 25:print("Sênior")
        elif idade > 25:print("MASTER TOP DAS GALAXIAS")