""" Implemente um programa que receba um número inteiro digitado pelo usuário e verifique se o
mesmo é primo. """

n = int(input("N: "))

for i in range (2, n - 1) :
    if (n % i) == 0 :
        print(n, "não é primo")
        break
else :
    print(n, "é primo")