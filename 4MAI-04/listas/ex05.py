""" Escreva um programa que receba como entrada uma palavra no formato string, depois cria e
imprime uma lista com os caracteres que formam a palavra. Exemplo:
Entrada = "Algoritmos"
Saída: ['A', 'l', 'g', 'o', 'r', 'i', 't', 'm', 'o', 's'] """

palavra = input("Palavra: ") # Recebe uma palavra
lista = [x for x in palavra] # Cria uma lista com cada caracter da palavra sendo um elemento da lista
print(lista)