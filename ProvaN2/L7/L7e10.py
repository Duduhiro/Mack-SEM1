""" 10) O código abaixo utiliza uma função chamada
sort() para ordenar os elementos de uma lista
(ordem crescente). Observe a figura ao lado:
Implemente uma função chamada ordena() que
faça o mesmo que a função sort() ilustrada no
código. """

lista = [8, 4, 3, 7, 9, 1, 2, 6]

def ordena (lista) :
    for i in range (len(lista) - 1) :
        for j in range (i + 1, len(lista)) :
            if lista[i] > lista[j] :
                lista[i], lista[j] = lista[j], lista[i]

ordena(lista)
print(lista)
