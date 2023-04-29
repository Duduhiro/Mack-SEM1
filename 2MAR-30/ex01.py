# Escreva um programa que apresente os n (1 ≤ n ≤ 20) primeiros termos da seguinte sequência: 1, 4,
# 9, 16, 25, ... Faça uma verificação para aceitar apenas números no intervalo de 1 a 20.

n = int(input("Insira um número entre 1 - 20: "))

while n < 1 or n > 20 :
    n = int(input("Valor incorreto, insira um número entre 1 - 20: "))

for i in range (1, n + 1) :
    print("%i | " %(i*i), end="")

