""" Escreva um programa que apresente os n (1 ≤ n ≤ 20) primeiros termos da seguinte sequência: 1, 4,
9, 16, 25, ... Faça uma verificação para aceitar apenas números no intervalo de 1 a 20. """

while True :
    n = int(input("N: "))
    if n >= 1 and n <= 20 :
        break
for i in range (1, n + 1) :
    print(i*i)