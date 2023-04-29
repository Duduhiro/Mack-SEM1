""" Faça um programa que calcule e apresente o fatorial de um número inteiro natural
entre 0 e 15 fornecido pelo usuário. Deverá ser feito a validação da entrada para que
seja digitado um número entre 0 e 15. Exemplo: 5! = 5 x 4 x 3 x 2 x 1=120. Por
definição 0! = 1. """

n = int(input("Insira um número entre 1 - 15: "))
result = 1

while n < 0 or n > 15 :
    n = int(input("Comando incorreto, insira um valor entre 1 - 15: "))

for i in range (1, n + 1) :
    result *= i

print("O fatorial do número %i é igual a %i" %(n, result))