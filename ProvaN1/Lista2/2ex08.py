""" Escreva um programa que receba três números inteiros quaisquer e apresente:
a) a soma dos quadrados dos três números;
b) o quadrado da soma dos três números. """
n = [0] * 3

for i in range (3) :
    n[i] = int(input(f"N{i + 1}: "))
print(f"Soma dos 3: {n[0] + n[1] + n[2]}")
print(f"Quadrado da soma dos 3: {(n[0] + n[1] + n[2]) * (n[0] + n[1] + n[2])}")