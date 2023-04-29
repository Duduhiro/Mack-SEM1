""" Escreva um programa que lê o tamanho do
lado de um quadrado e imprime um
quadrado daquele tamanho com asteriscos
e espaços em branco. Seu
programa deve funcionar para
quadrados com lados de todos
os tamanhos entre 1 e 20.
Exemplo: para lado igual a 5: """

n = int(input("Insira o lado do quadrado: "))

for i in range (n) :
    if i not in [0 , n - 1] :
        print('*'.ljust(n*2-2) + '*')
    else :
        print('* ' * n)

