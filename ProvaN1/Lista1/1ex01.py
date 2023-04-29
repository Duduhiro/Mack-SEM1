# Elabore um programa que leia três notas, calcule e mostre a média aritmética entre elas.
n = 0
for i in range (3) :
    n += float(input("Insira uma nota: "))
print(f"Média aritmética {n / 3:.2f}")
