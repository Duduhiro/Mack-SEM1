""" Implemente um programa que receba um número inteiro digitado pelo usuário e verifique se o
mesmo é primo. """

n = int(input("Insira um número para verificar se ele é primo: "))
seletor = 1

for i in range (2, n - 1) :
    if n % i == 0 :
        seletor = 1
    else :
        seletor = 0
if seletor == 0 :
    print("O número %i é primo" %(n))
else :
    print("O número %i não é primo" %(n))