# 1) Elabore um programa que leia três notas, calcule e mostre a média aritmética entre elas.

nota = 0
for i in range (3) :
    nota += int(input("Nota: "))
print(f'Média: {nota / 3}')