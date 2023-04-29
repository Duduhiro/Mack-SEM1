"""Objetivo do projeto: 1.0 - desenvolver uma calculadora simples que possua as funções básicas 
como adição, subtração, divisão e multiplicação. O foco principal é desenvolver um programa que
funcione de acordo com o input no terminal, depois, desenvolver uma GUI para tornar o programa
mais agradável e funcional para o usuário"""

import math

def soma (n1, n2) :
    #função para somar 2 números
    result = n1 + n2
    return result
def subt (n1, n2) :
    #função para subtrair 2 números
    result = n1 - n2
    return result
def multi (n1, n2) :
    #função para multiplicar 2 números
    result = n1 * n2
    return result
def divi (n1, n2) :
    #função para dividir dois números
    if n2 == 0 :
        print("Impossível dividir por 0")
    else :
        result = n1 / n2
        return result
    
print("CALCULADORA 3000")
print("Funcionamento: o programa aceita contas de adição, subtração, multiplicação e divisão.\n"
      + "Entretanto, as contas só podem possuir 2 números.\nType EXIT to shutdown")

sinal = ""
while sinal != "exit" :
    sinal = input("+ | - | * | / | exit : ")
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    if sinal == "exit" : 
        break
    elif sinal == "+" :
        result = soma(n1, n2)
    elif sinal == "-" :
        result = subt(n1, n2)
    elif sinal == "*" :
        result = multi(n1, n2)
    elif sinal == "/" :
        result = divi(n1, n2)
    print("%f %s %f = %f" %(n1, sinal, n2, result))