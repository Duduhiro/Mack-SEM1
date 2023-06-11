""" 1) Faça um programa que receba um número inteiro e informe se ele é divisível por 10 e, 
independentemente disso, é divisível por 5; e, independentemente disso, é divisível por 2; ou se não 
é divisível por nenhum destes. """

n = int(input("N: "))
counter = 0
if n % 10 == 0 :
    counter += 1
    print('Divisível por 10')
if n % 5 == 0 :
    print('Divisível por 5')
    counter += 1
if n % 2 == 0 :
    print('Divisível por 2')
    counter += 1
if counter == 0 :
    print('Não é divisível por 2, 5 ou 10')
