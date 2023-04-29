""" Faça um programa que leia um valor N
inteiro e positivo, valide a entrada digitada
e, depois, calcule e mostre o valor de E,
conforme a fórmula a seguir: """

n = int(input("Insira um valor positivo: "))
result = 1

for i in range (1 , n + 1) :
    fatorial = 1
    for j in range (1, i + 1) :
        fatorial *= j
    result += 1 / fatorial
print(result)