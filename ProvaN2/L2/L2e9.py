""" 9) Faça um programa que coloque dois nomes em ordem alfabética. """
nome1 = input("Nome1: ")
nome2 = input("Nome2: ")
if nome2 < nome1 :
    nome1, nome2 = nome2, nome1
print(f'{nome1}\n{nome2}')