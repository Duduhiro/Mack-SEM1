""" 5) Faça um programa que apresente se o número que o usuário digitou é divisível por 3 e por 5 ao 
mesmo tempo. """

n = int(input("N: "))

if n % 5 == 0 and n % 3 == 0 :
    print('O número é divisível por 3 e 5')
else :
    print('O número não é divisível por 3 e 5')
