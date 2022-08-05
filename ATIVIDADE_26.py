#26 - Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "a" // Em que posição ela apareec pela primeira vez // Em que posição ela aparece a última vez;
frase = "batata"
x = frase.find("a")
z = frase.rfind("a")
y = frase.count("a")
print(frase)
print("Aparece pela primeira vez em: ",x)
print("Aparece na ultima vez em: ",z)
print("a se repete :",y,"x")