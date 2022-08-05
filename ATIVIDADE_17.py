#17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# a² + b² = c²
a = float(input("DIGITE UM CATETO: "))
b = float(input("DIGITE O OUTRO CATETO: "))
c = (a**2 + b**2)**(1/2)
print("Tua hipotenusa mede {}".format(c))