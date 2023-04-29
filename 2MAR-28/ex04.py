# Faça um programa que solicite números inteiros e determine a soma e quantidade de números
# digitados enquanto o usuário não digitar -1. Ao final é informado a soma e quantidade de números
# digitados, exceto o -1.

soma = 0
contador = 0 
n = 0 

while n != -1 :
    n = int(input("Insira um número (-1 para encerrar): "))
    if n != -1 :
        if n % 2 == 0 :
            print("Par")
        else :
            print("Impar")
        contador += 1
        soma += n
    
print("Foram inseridos %i números e a soma de todos os números é %i" %(contador, soma))