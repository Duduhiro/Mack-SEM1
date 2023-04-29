""" Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de
Fahrenheit para Celsius(para isso o usuário deve digitar F) e de Celsius para Fahrenheit (neste caso o usuário
deve digitar C).
Para a construção do programa você deve escrever as seguintes funções:
• exibeMsg() - apenas exibe uma mensagem para ao usuário dizendo o que o programa faz e
informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não tem
retorno;
• verificaOpcao() - a função não tem parâmetro de entrada e retorna “F” ou “C” (fazer a validação
para que o usuário só digite F ou C);
• verificaIntervalo() - a função não tem parâmetro de entrada e retorna os valores inicial e final
do intervalo (fazer a validação para que o valor inicial seja menor que o valor final);
• exibeFahrenheitToCelsius(inicio, fim)  essa função recebe como entrada o intervalo de
temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida
para Celsius;
• exibeCelsiusToFahrenheit(inicio, fim)  essa função recebe como entrada o intervalo de
temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida
para Fahrenheit """

def exibeMsg () :
    print("C - celsius para fahrenheit\nF - fahrenheit para celsius")

def verificaOpcao () :
    while True :
        text = input("F or C: ")
        if text.upper() == "F" or text.upper() == "C" :
            break
    return text

def verificaIntervalo () :
    while True :
        inicial = int(input("Inicio: "))
        final = int(input("Final: "))
        if inicial < final :
            break
    return inicial, final

def exibeFahrenheitToCelsius (inicio, final) :
    for i in range (inicio, final + 1) :
        print(f"{i} ° F <-> {(i - 32) / 1.8:3.1f} ° C")


def exibeCelsiusToFahrenheit (inicio, final) :
    for i in range (inicio, final + 1) :
        print(f"{i:3.1f} ° C <-> {i * 1.8 + 32:.1f} ° F")

def main () :
    exibeMsg()
    text = verificaOpcao()
    a = verificaIntervalo()
    if text == "C" :
        exibeCelsiusToFahrenheit(a[0], a[1])
    else :
        exibeFahrenheitToCelsius(a[0], a[1])

main()