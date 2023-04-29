""" Modifique o programa escrito no exercício anterior de modo que não sejam feitas mais do que 3
comparações para decidir a ordem em que os elementos deverão ser escritos. """

n = [0] * 3

for i in range (3) :
    n[i] = int(input(f"Insira o número {i + 1}: "))
list.sort(n)
print(n[0], n[1], n[2])