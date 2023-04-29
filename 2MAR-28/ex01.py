# Faça um programa que solicite 5 números inteiros e determine se eles são ímpares ou pares. 

for i in range (5) :
    n = int(input("Insira um número: "))
    if n % 2 == 0 :
        print("O número é par")
    else :
        print("O número é impar")