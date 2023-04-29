""" Faça um programa para ler três números inteiros positivos do teclado e realizar alguns cálculos. Para
tal, cria as seguintes funções:
• entrada(): responsável por solicitar ao usuário que informe um valor inteiro, fazendo a
validação para garantir que o valor seja positivo e retornando o valor informado.
• calculaMedia(x,y,z): que computa a média aritmética dos parâmetros informados.
• main(): que apresenta uma mensagem informando o propósito do programa e realiza as tarefas
esperadas invocando as sub-rotinas criadas anteriormente. """

def entrada () :
    while True :
        n = int(input("N: "))
        if n > 0 :
            break
    return n

def calculaMedia (x, y, z) :
    media = (x + y + z) / 3
    return media

def main () :
    print('Esse programa calcula a média aritmética de 3 valores')
    x = entrada()
    y = entrada()
    z = entrada()
    print(f"A média é {calculaMedia(x, y, z)}")

main()

