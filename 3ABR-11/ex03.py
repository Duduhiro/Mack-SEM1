""" Faça um programa que calcule e apresente o fatorial de um número inteiro e natural fornecido
pelo usuário.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.
Por definição 0! = 1 """

n = int(input("Insira um número para ser calculado o seu fatorial: "))
result = 1

for i in range (1, n + 1) :
    result *= i    
print("O fatorial de %i é %i" %(n, result))