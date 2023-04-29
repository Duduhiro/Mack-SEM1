""" Crie um algoritmo em Python que leia um número inteiro (e diferente de zero) e mostre uma
mensagem indicando se este número é positivo ou negativo.
 """

while True :
    n = int(input("N: "))
    if n != 0 : 
        break
if n > 0 :
    print("Positivo")
else :
    print("Negativo")
