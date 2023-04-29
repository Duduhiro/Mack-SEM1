""" A conversão de graus Fahrenheit para Celsius é obtida pela fórmula: 𝐶 = (5 / 9) (𝐹 − 32)
Escreva um programa que calcule e apresente uma tabela de graus Celsius em função de graus
Fahrenheit que variem de 50 a 150, de 1 em 1. """

for i in range (50, 151) :
    celsius = (5 / 9) * (i - 32)
    print("%i Fahrenheit = %.2f Celsius" %(i, celsius))
