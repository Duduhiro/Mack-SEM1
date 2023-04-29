# Faça um programa que leia um número inteiro (e diferente de zero) e mostre
# uma mensagem indicando se este número é positivo ou negativo.

print("Esse programa identifica se um número é positivo ou negativo")
n = int(input("Insira um número: "))
if n >= 0 :
    print("O número %i é positivo" %(n))
else :
    print("O número %i é negativo" %(n))