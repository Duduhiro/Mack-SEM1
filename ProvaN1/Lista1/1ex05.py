""" Altere o programa anterior para conter mais três variáveis, com o preço unitário da fruta,
verdura e legume. Estas variáveis devem armazenar números e não strings. Depois, mostre o
preço de cada produto após o nome (nome ao lado do preço, por exemplo: “Maça: 10”) """

comidas = [
    "Morango", 6.40, "Alface", 4.60, "Beringela", 7.50
]

for i in range (0, 6, 2) :
    print(comidas[i], end=" ")
    print(comidas[i + 1])