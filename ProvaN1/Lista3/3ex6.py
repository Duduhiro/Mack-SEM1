""" Faça um programa que, lido três valores inteiros, escreva-os na tela em ordem crescente. """

n = [0] * 3

for i in range (3) :
    n[i] = int(input(f"Insira o número {i + 1}: "))
list.sort(n)
print(n[0], n[1], n[2])
