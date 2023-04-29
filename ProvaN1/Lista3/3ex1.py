""" Faça um programa que receba um número inteiro e informe se ele é divisível por 10 e,
independentemente disso, é divisível por 5; e, independentemente disso, é divisível por 2; ou se não
é divisível por nenhum destes. """

n = int(input("N: "))
contador = 0

if n % 10 == 0 :
    print("Esse número é divisível por 10")
else :
    contador += 1
if n % 5 == 0 :
    print("Esse número é divisível por 5")
else :
    contador += 1
if n % 2 == 0 :
    print("Esse número é divisível por 2")
else : 
    contador += 1
if contador == 3 :
    print("Esse número não é divisível por 10, 5 ou 2")
