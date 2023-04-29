""" Como você faria para construir o gráfico caso trabalhássemos com valores positivos e negativos?
Tente implementar e depois teste sua ideia para os conjuntos de valores: [-3, 5, 1,-4, 3, 2] e
[-5,-2,-1, 0,-1,-2,-5]
"""

a = [-3, 5, 1,-4, 3, 2]

for i in range (len(a)) :
    if a[i] < 0 :
        print(" " * (abs(min(a)) - abs(a[i])), end="")
        print("#" * abs(a[i]))
    else :
        print(" " * abs(min(a)), end="")
        print("#" * a[i])