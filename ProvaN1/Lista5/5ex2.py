""" Faça um programa que calcule e apresente o fatorial de um número inteiro natural
entre 0 e 15 fornecido pelo usuário. Deverá ser feito a validação da entrada para que
seja digitado um número entre 0 e 15. Exemplo: 5! = 5 x 4 x 3 x 2 x 1=120. Por
definição 0! = 1. """
from math import factorial

while True : 
    n = int(input("N: "))
    if n >= 0 and n <= 15 :
        break

print(factorial(n))