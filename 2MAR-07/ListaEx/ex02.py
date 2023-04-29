# Faça um programa que apresenta o maior de dois números inteiros (diferentes)
# lidos do usuário.

print("Esse programa identifica qual número inserido é maior")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
if n1 != n2 :
    if n1 > n2 :
        print("O número %i é maior que o número %i" %(n1, n2))
    else :
        print("O número %i é maior que o número %i" %(n2, n1))