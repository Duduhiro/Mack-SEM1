# Programa que lê um inteiro positivo n e imprime o valor da soma destes números: 1 + 2 + 3 + ... +
# n.

n = int(input("Insira um número: "))

resultado = 0

for i in range (n) :
    resultado += (i + 1)

print("A soma do número %i com os seus antecessores é de %i" %(n, resultado))