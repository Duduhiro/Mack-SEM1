""" 1. Faça um programa, utilizando funções, que receba três números inteiros e positivos, e que forneça a
soma desses três números.
Para este exercício crie três funções:
• entrada() - retorna um número digitado (fazer a verificação se é positivo);
• calculaSoma(a, b, c) - recebe 3 números inteiros e positivos e retorna a soma deles;
• main() - chamada das funções criadas (chama 3 vezes a entrada, sendo uma para cada número e a
função para somar) e depois mostre o resultado. """

def entrada () :
    while True :
        n = int(input("N: "))
        if n > 0 :
            break
    return n

def calculaSoma (a, b, c) :
    return a + b + c

def main () :
    a = entrada()
    b = entrada()
    c = entrada()
    print(f"Soma = {calculaSoma(a, b, c)}")

main()