# Escreva um programa que apresente os n (1 <= n <= 20) primeiros termos da seguinte sequência:
# 1, 4, 9, 16, 25, ...

n = 0
while n < 1 or n > 20 :
    n = int(input("Insira quantos termos você quer ver na sequência: "))
for i in range (1, n + 1) :
    print(i*i)
