""" Faça um programa que receba uma frase como entrada (sem pontuação) e conte o número de
palavras. """

frase = input("Frase: ")
quant = frase.count(' ') + 1
print(f"Palavras: {quant}")