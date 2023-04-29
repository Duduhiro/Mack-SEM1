""" Faça um programa que leia um número n (positivo) que indique quantos valores inteiros e
positivos devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial desse
valor """

n = int(input("Insira quantos valores serão lidos: "))

for i in range (n) :
    result = 1
    m = int(input("Insira um número para ser calculado o seu fatorial: "))
    for j in range (1, m + 1) :
        result *= j
    print("O fatorial de %i é %i" %(m, result))