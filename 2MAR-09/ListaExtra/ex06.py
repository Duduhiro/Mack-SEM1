# Faça um programa que, lido três valores inteiros, escreva-os na tela em ordem crescente

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))

if n1 < n2 :
    if n1 < n3 :
        if n2 < n3 :
            print(n1, n2, n3)
        else :
            print(n1, n3, n2)
    else : 
        print(n3, n1, n2)
else :
    if n1 < n3 :
        print(n2, n1, n3)
    else :
        if n2 < n3 :
            print(n2, n3, n1)
        else :
            print(n3, n2, n1)