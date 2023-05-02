""" 1) Faça um programa que leia um vetor de 5 números inteiros e mostre-os. Deverá ter
duas funções, uma para entrada pelo teclado e inserção na lista dos números e uma outra
função para a impressão da lista. Dica: utilize a função append() em python para inserir
elementos no vetor.  """

def registro () :
    vetor = []
    for i in range (5) :
        n = int(input("N: "))
        vetor.append(n)
    return vetor

def printar (lista) :
    for i in range (len(lista)) :
        print(f"{lista[i]} | ", end="")

lista = registro()
printar(lista)