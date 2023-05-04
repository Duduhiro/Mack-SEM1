""" Escreva um programa que receba como entrada uma palavra no formato string, depois cria e
imprime uma lista com os caracteres que formam a palavra. Exemplo:
Entrada = "Algoritmos"
Saída: ['A', 'l', 'g', 'o', 'r', 'i', 't', 'm', 'o', 's'] """

palavra = input("Palavra: ")
lista = [x for x in palavra]
print(lista)