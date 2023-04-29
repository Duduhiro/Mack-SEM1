""" Implemente um procedimento graphBar que, recebendo cinco valores
positivos como parâmetro, exibe um gráfico de barras na tela como é dado na
figura ao lado.
Faça também um programa com valores a sua escolha para testar a sua função.
EX: supondo a chamada graphBar(2,3,5,4,1) """

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