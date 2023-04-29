# Escreva um programa que calcule e apresente a soma da seguinte série:
divider = 1
result = 0

for i in range (1, 101, 2) :
    result += i / divider
    divider += 1
print(result)