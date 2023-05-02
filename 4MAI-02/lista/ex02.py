""" 2) Faça um programa que leia um vetor de 10 números inteiros e mostre-os na ordem
inversa. Deverá ter duas funções, uma para entrada pelo teclado e inserção dos números
lidos na lista e outra função que coloca os elementos da lista em ordem inversa e imprime
a lista ordenada inversamente. Dica: utilize a função reverse() disponibilizada pelo python. """

def registro () :
    vetor = []
    for i in range (10) :
        n = int(input("N: "))
        vetor.append(n)
    vetor.sort()
    return vetor

def ordena_lista (lista) :
    lista = lista[::-1]
    print(lista)

lista = registro()
ordena_lista(lista)