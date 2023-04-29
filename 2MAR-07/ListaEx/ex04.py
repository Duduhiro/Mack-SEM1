# Faça um programa que apresente se o número que o usuário digitou é divisível por 3 e por 5 ao mesmo tempo.

print("Esse programa verifica se um número é divisível por 3 e por 5")
n = float(input("Insira um valor: "))

if n % 5 == 0 and n % 3 == 0:
    print("O número %f é divisível por 3 e por 5" %(n))
else:
    print("O número %f não é divisível por 3 e por 5" %(n))

