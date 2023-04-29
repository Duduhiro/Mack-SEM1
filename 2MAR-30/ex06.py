""" Fazer um programa que leia um valor inteiro
X do teclado e depois calcule e escreva o
resultado do seguinte somatório: """
import math

x = int(input("Insira um valor positivo: "))
result = math.pow(x, 25)

for i in range (2, 26, 2) :
    result -= math.pow(x, 25 - i) / i
    result += math.pow(x, 24 - i) / (i + 1)
print(result)