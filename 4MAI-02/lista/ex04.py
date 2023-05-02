""" 4) Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes e
quantas vogais foram lidas. Imprima o vetor e as quantidades solicitadas. Implemente uma
primeira função para criar a lista de caracteres. Uma segunda função para contar o número
de vogais, uma terceira função contar o número de consoantes e uma quarta função para
imprimir o vetor e as quantidades contabilizadas """

def cria_lista () :
    lista = []
    for i in range (10) :
        while True :
            strg = input("Caracter: ")
            if len(strg) == 1 :
                break
            else :
                print("Error! 1 character allowed!")
        lista.append(strg)
    return lista

def conta_vogal (lista) :
    vogal = 0
    consoante = 0
    for i in lista :
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
            vogal += 1
        else :
            consoante += 1
    return vogal, consoante

def imprime (lista, vogal, consoante) :
    print(lista)
    print(f"Vogal: {vogal}")
    print(f"Consoante: {consoante}")

lista = cria_lista()
letras = conta_vogal(lista)
imprime(lista, letras[0], letras[1])