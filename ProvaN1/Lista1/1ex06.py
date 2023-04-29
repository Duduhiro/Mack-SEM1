""" Escreva um programa em Python que o usuário digita dois números inteiros e armazena em
duas variáveis n1 e n2, o seu programa deve trocar os valores dessas variáveis, de maneira que
o valor de n1 seja igual ao de n2 e vice-versa, e depois deve exibir os números lidos com valores
trocados. """

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n1, n2 = n2, n1
print(f"N1 = {n1} | N2 = {n2}")