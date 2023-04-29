""" Escreva um programa que lê o tamanho do lado de um quadrado e imprime um
quadrado daquele tamanho com asteriscos e espaços em branco. Seu
programa deve funcionar para quadrados com lados de todos
os tamanhos entre 1 e 20. Exemplo: para lado igual a 5: """

n = int(input("N: "))

for i in range (n) :
    print("*", end=" ")
print()
for i in range(0, n - 2) :
    print("*", end=" ")
    print("  " * (n - 2), end="")
    print("*",)
for i in range (n) :
    print("*", end=" ")
