""" Construa um procedimento chamado TabelaDeTemperatura para exibir na tela uma tabela de
correspondência de medidas de temperatura, apresentando em cada linha o valor em °C e seu
equivalente em °F. Essa sub-rotina deve receber dois parâmetros, mínimo e máximo, que
determinam a faixa de valores (intervalo) em °C que a tabela conterá. Um terceiro parâmetro,
opcional, indica o espaçamento entre os valores e que se nada for informado deve ser igual a 5.
Obs: Para conversão, utilize a função implementada no exercício #1. """

def tabela_temperatura (min, max, interval) :
    deg_cels = min
    temp_list = []
    
    while deg_cels <= max :
        temp_info = {
        'celsius' : "",
        'fahreinheit' : ""
    }
        temp_info['celsius'] = deg_cels
        temp_info['fahreinheit'] = 9/5 * deg_cels + 32
        deg_cels += interval
        temp_list.append(temp_info)
    return temp_list

min = int(input("Min: "))
max = int(input("Max: "))
interval = int(input("Interval: "))
result = tabela_temperatura(min, max, interval)
for i in range (len(result)) :
    print(f"{result[i]['celsius']} ° C <-> {result[i]['fahreinheit']:.2f} ° F")