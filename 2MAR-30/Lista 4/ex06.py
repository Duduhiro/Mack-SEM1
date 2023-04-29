""" Faça um programa que calcule o fatorial de um número N inteiro e positivo (N!). Saiba que:
N! = 1 x 2 x 3 .... x (N -1) x N
0! = 1 """

n = int(input("Insira um número para ser calculado o seu fatorial: "))
result = 1

for i in range (1, n + 1) :
    result *= i
print("O fatorial de %i é %i" %(n, result))