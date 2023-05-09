""" Desenvolva um código em Python que dado um valor numérico inteiro digitado pelo usuário,
imprima cada um dos seus dígitos por extenso.
Exemplo: Entre com um número: 4571
Resultado: quatro, cinco, sete, um. """

n = int(input("N: ")) # Recebe um número inteiro
n = str(n) # Transforma o número em uma String
for i in n : # Itera entre os elementos da string e printa o número por extenso
    if i == '0' :
        print('Zero ', end='')
    elif i == '1' :
        print('Um ', end='')
    elif i == '2' :
        print('Dois ', end='')
    elif i == '3' :
        print('Três ', end='')
    elif i == '4' :
        print('Quatro ', end='')
    elif i == '5' :
        print('Cinco ', end='')
    elif i == '6' :
        print('Seis ', end='')
    elif i == '7' :
        print('Sete ', end='')
    elif i == '8' :
        print('Oito ', end='')
    elif i == '9' :
        print('Nove ', end='')
