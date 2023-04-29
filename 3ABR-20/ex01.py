""" Faça um programa para ler três números inteiros positivos do teclado e realizar alguns cálculos. Para
tal, cria as seguintes funções:
• entrada(): responsável por solicitar ao usuário que informe um valor inteiro, fazendo a
validação para garantir que o valor seja positivo e retornando o valor informado.
• calculaMedia(x,y,z): que computa a média aritmética dos parâmetros informados.
• main(): que apresenta uma mensagem informando o propósito do programa e realiza as tarefas
esperadas invocando as sub-rotinas criadas anteriormente.
"""

def entrada () :
    while True :
        n = int(input("N: "))
        if n > 0 :
            break
    return n

def calcula_media (x, y, z) :
    return (x + y + z) / 3

def main () :
    print("Esse programa calcula a média de 3 números")
    n1 = entrada()
    n2 = entrada()
    n3 = entrada()
    print(f"A média é {calcula_media(n1, n2, n3):.2f}")

main()