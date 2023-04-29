""" Modifique a função implementada no exercício #5 para trabalhar com uma lista, permitindo assim
que seja construídos gráficos para conjuntos com qualquer quantidade de elementos.
 """

def graph_bar (list) :
    for i in range (len(list)) :
        print('#' * list[i])

graph_values = []
while True :
    n = int(input("Graph value (-1 to exit): "))
    if n == -1 :
        break
    graph_values.append(n)
graph_bar(graph_values)