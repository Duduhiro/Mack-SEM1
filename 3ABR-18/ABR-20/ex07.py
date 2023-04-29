""" Como você faria para construir o gráfico caso trabalhássemos com valores positivos e negativos?
Tente implementar e depois teste sua ideia para os conjuntos de valores: [-3, 5, 1,-4, 3, 2] e
[-5,-2,-1, 0,-1,-2,-5] """

list_a = [-3, 5, 1,-4, 3, 2]
list_a.sort()
for i in range (len(list_a)) :
    if list_a[i] < 0 :
        print(" " * (abs(list_a[0]) - abs(list_a[i])), end="")
        print("#" * (list_a[i] * -1))
    else :
        print(" " * (list_a[0] * -1), end="")
        print("#" * list_a[i])
