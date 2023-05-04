""" O código abaixo utiliza uma função chamada
sort() para ordenar os elementos de uma lista
(ordem crescente). Observe a figura ao lado:
Implemente uma função chamada ordena() que
faça o mesmo que a função sort() ilustrada no
código. """

def ordena (lista) :
    for i in range (len(lista)) :
        for j in range (len(lista) - 1) :
            if j == i :
                j += 1
            if lista[i] <= lista[j] :
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [8, 1, 4, 9, 2, 0, 7]

print(ordena(lista))