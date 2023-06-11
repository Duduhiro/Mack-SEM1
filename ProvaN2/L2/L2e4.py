""" 4) Implemente um programa que apresenta o maior de dois números inteiros (diferentes) lidos do 
usuário. """

n1 = int(input("N1: "))
n2 = int(input("N2: "))
if n1 < n2 :
    n1, n2 = n2, n1
print(f'Maior: {n1}')
