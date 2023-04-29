""" Construa um procedimento chamado TabelaDeTemperatura para exibir na tela uma tabela de
correspondência de medidas de temperatura, apresentando em cada linha o valor em °C e seu
equivalente em °F. Essa sub-rotina deve receber dois parâmetros, mínimo e máximo, que
determinam a faixa de valores (intervalo) em °C que a tabela conterá. Um terceiro parâmetro,
opcional, indica o espaçamento entre os valores e que se nada for informado deve ser igual a 5.
Obs: Para conversão, utilize a função implementada no exercício #1. """

#Now my programs have minecraft font =)

def tabela_de_temperatura (min, max, interval) :
    # Populate lista_temps with dictionaries about celsius and fahrenheit
    celsius = min
    lista_temps = []
    while celsius <= max :
        temp_dict = { # initiate the celsius and fahrenheit dict
            'celsius' : '',
            'fahrenheit' : ''
        }
        temp_dict['celsius'] = celsius
        temp_dict['fahrenheit'] = 9 / 5 * celsius + 32
        celsius += interval
        lista_temps.append(temp_dict)
    return lista_temps

min = int(input("Min: "))
max = int(input("Max: "))
interval = int(input("Interval: "))
result = tabela_de_temperatura(min, max, interval)

for i in range (len(result)) :
    print(f"{result[i]['celsius']} ° C <-> {result[i]['fahrenheit']:.2f} ° F")
    print('to com sono zZZZzzZzZzZz')