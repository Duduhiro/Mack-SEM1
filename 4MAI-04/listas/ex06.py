""" Faça um programa que receba uma frase como entrada (sem pontuação) e conte o número de
palavras. """

frase = input("Frase: ") # Recebe uma frase
quant = frase.count(' ') + 1 # Conta quantas palavras essa frase possui ao contar os espaços em branco entre as palavras
print(f"Palavras: {quant}")