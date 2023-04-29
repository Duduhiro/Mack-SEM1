""" Faça um programa que calcule o fatorial de um número N inteiro e positivo (N!). Saiba que:
N! = 1 x 2 x 3 .... x (N -1) x N
0! = 1 """
from math import factorial

n = int(input("N: "))
print(f"N fatorial = {factorial(n)}")