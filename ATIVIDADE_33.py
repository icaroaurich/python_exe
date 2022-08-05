#33- Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
pnumero = 1
snumero = 2
tnumero = 3
if pnumero > snumero and pnumero > tnumero:print("{} é o maior número".format(pnumero))
elif snumero > pnumero and snumero > tnumero:print("{} é o maior número".format(snumero))
elif tnumero > snumero and tnumero > pnumero:print("{} é o maior número".format(tnumero))
if pnumero < snumero and pnumero < tnumero:print("{} é o menor número".format(pnumero))
elif snumero < pnumero and snumero < tnumero:print("{} é o menor número".format(snumero))
elif tnumero < snumero and tnumero < pnumero:print("{} é o menor número".format(pnumero))