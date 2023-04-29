""" Implemente um programa que apresenta o maior de dois números inteiros (diferentes) lidos do
usuário. """

n = [0] * 2

n[0] = int(input("N1: "))
n[1] = int(input("N2: "))
list.sort(n)
print(f"O maior número é {n[1]}")