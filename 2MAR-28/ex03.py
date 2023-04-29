# Faça um programa que solicite números inteiros e determine se eles são ímpares ou pares
# enquanto o usuário não digitar -1. Ao final é informado a quantidade de números digitados, exceto
# o -1. 

contador = 0 
n = 0 

while n != -1 :
    n = int(input("Insira um número (-1 para encerrar): "))
    if n % 2 == 0 :
        print("Par")
    else :
        print("Impar")
    contador += 1

print("Foram inseridos %i números" %(contador))