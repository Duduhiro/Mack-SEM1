# Modifique o programa escrito no exercício anterior de modo que não sejam feitas mais do que 3
# comparações para decidir a ordem em que os elementos deverão ser escritos.

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: ")) 

if n1 > n2 :
    n4 = n1
    n1 = n2
    n2 = n4

if n1 > n3 :
    n4 = n1
    n1 = n3
    n3 = n4

if n2 > n3 :
    n4 = n2
    n2 = n3
    n3 = n4

print(n1, n2, n3)