""" Faça um programa modularizado em Python com as seguintes funções:

a) atualiza_preco(valor): a função deve receber como parâmetro o valor de um 
produto, calcular e retornar este valor com aumento de 10%

b) taxa(valor): a função recebe como parãmetro o valor do produto atualizado, 
calcula e retorna o valor da taxa de 2.5% sobre o valor do produto atualizado 
(após a chamada da função atualiza_preco).

c) main(): terá o programa principal que deve, nesta ordem, fazer a entrada via 
teclado (digitada pelo usuário) do valor do produto, depois chamar as funções atualiza_preco 
e taxa e apresentar os valores calculados do valor atualizado com 2 casas decimais e do valor 
da taxa com 2 casas decimais.

Ao final chame a função main() para que o programa seja executado. """

def atualiza_preco (valor) :
    return valor * 1.10

def taxa (valor) :
    return valor * 0.025

def main () :
    produto = float(input())
    preco = atualiza_preco(produto)
    tax = taxa(preco)
    print(f'{preco:.2f}')
    print(f'{tax:.2f}')

main()