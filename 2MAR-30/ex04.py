""" Faça um programa que recebe a
altura de um triangulo em um
número inteiro e imprima-o
utilizando asteriscos. Veja o
exemplo: para uma entrada
igual a 5 """

n = int(input("Insira a altura do triangulo: "))

for i in range (1, n + 1): 
    print("*" * i)