""" 2) Implemente um programa que receba um número inteiro digitado pelo usuário e verifique se o 
mesmo é primo. """

n = int(input("N: "))

for i in range(2, int(n / 2) + 1) :
    if n % i == 0 :
        print('O número não é primo')    
        break
else:
    print('O número é primo')