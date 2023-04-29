# 1. Faça um programa que leia 4 notas bimestrais de uma disciplina, calcule e mostre a média aritmética do
# bimestre.

print("----------- AVG CALCULATOR -----------")
nota = float(0)
for i in range (4):
    nota += float(input(f"Insira a {i + 1}ª nota: "))
nota = nota / 4
print("A média aritmética do bimestre é de: %.1f" %(nota))
