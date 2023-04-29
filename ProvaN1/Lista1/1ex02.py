""" Elabore um programa que receba três notas e seus respectivos pesos, calcule e mostre a média
ponderada dessas notas. """
total = 0
pesoTotal = 0
for i in range (3) :
    nota = float(input(f"Insira a nota {i + 1}: "))
    peso = int(input(f"Insira o peso da nota {i + 1}: "))
    pesoTotal += peso
    total += nota * peso
print(f"A nota ponderada é de {total / pesoTotal:.2f}")