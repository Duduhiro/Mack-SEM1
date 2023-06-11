""" 2) Elabore um programa que receba três notas e seus respectivos pesos, calcule e mostre a média 
ponderada dessas notas """
total = 0
pesoTotal = 0
for i in range (3) :
    nota = int(input("Nota: "))
    peso = int(input("Peso: "))
    total += nota * peso
    pesoTotal += peso
print(f'Média {total / pesoTotal}')