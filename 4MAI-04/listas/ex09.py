""" Crie um vetor de tamanho 20, inicialmente com valores None. Depois, preencha cada posição
com valores randômicos (0 a 100). Faça uma função para encontrar o maior e o menor
elemento e imprimir. """
import random

def find_max_min (lista) :
    # Define função de achar o max e min de uma lista ao ordena-la e depois pegar o primeiro e o ultimo elemento
    lista.sort()
    return lista[0], lista[len(lista) - 1]

vetor = [None] * 20

for i in range (len(vetor)) :
    vetor [i] = random.randint(0, 100)

pos = find_max_min(vetor)
print(vetor)
print(f'Min: {pos[0]} | Max: {pos[1]}')
