""" O código abaixo utiliza uma função chamada
sort() para ordenar os elementos de uma lista
(ordem crescente). Observe a figura ao lado:
Implemente uma função chamada ordena() que
faça o mesmo que a função sort() ilustrada no
código. """

def ordena (lista) :
    # Função para ordenar uma lista
    for i in range (len(lista) - 1) : # Itera sobre os elementos da lista com o uso de neested loops
        for j in range (i + 1, len(lista)) : 
            if lista[i] > lista[j] : 
                lista[i], lista[j] = lista[j], lista[i]
        print(lista)
    return lista

lista = [8, 1, 4, 9, 2, 0, 7, 3, 5, 11, 4 , 5]

print(ordena(lista))