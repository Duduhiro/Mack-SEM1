""" a) atualiza_preco(valor): a função deve receber como parâmetro o valor de um produto, 
calcular e retornar este valor com aumento de 10%

b) taxa(valor): a função recebe como parãmetro o valor do produto atualizado, calcula e 
retorna o valor da taxa de 2.5% sobre o valor do produto atualizado (após a chamada da função atualiza_preco).

c) main(): terá o programa principal que deve, nesta ordem, fazer a entrada via teclado 
(digitada pelo usuário) do valor do produto, depois chamar as funções atualiza_preco e taxa e 
apresentar os valores calculados do valor atualizado com 2 casas decimais e do valor da taxa com 2 casas decimais. """

def atualiza_preco (valor) :
    return valor * 1.10

def taxa (valor) :
    return valor * 0.025

def main () :
    valor = float(input())
    valor = atualiza_preco(valor)
    tax = taxa(valor)
    print(f"{valor:.2f}")
    print(f"{tax:.2f}")
