""" 3) Faça um programa que leia 4 notas com valores reais entre 0 a 10, mostre as notas e a
média na tela. Implemente três funções, uma primeira de entrada para ler cada nota,
validar se cada nota está no intervalo entre 0 e 10 e inserir na lista. Uma segunda função
para calcular a média e uma terceira função para imprimir as notas e média. Supor que
esta terceira função recebe como argumento a média calculada pela segunda função. Dica:
utiliza a função sum() disponibilizada pelo python.  """

def entrada () :
    notas = []
    for i in range (4) :
        while True :
            n = int(input("Nota: "))
            if n <= 10 and n >= 0 : 
                break
        notas.append(n)
    return notas

def calcula_media (lista) :
    media = sum(lista) / len(lista)
    return media

def imprime(lista, media) :
    for i in range (len(lista)) :
        print(f"N{i + 1}: {lista[i]}")
    print(f"Média: {media}")

notas = entrada()
media = calcula_media(notas)
imprime(notas, media)
