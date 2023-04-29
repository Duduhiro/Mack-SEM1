# Faça um programa que coloque dois nomes em ordem alfabética.

print("Esse programa coloca dois nomes em ordem alfabética")

s1 = input("Insira o primeiro nome: ")
s2 = input("Insira o segundo nome: ")

if s1 < s2 :
    print("O primeiro nome é %s e o segundo é %s" %(s1, s2))
else :
    print("O primeiro nome é %s e o segundo é %s" %(s2, s1))