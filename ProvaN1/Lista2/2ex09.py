""" Faça um programa que coloque dois nomes em ordem alfabética. """
nome = [""] * 2
nome[0] = input("Nome 1: ")
nome[1] = input("Nome 2: ")
if nome [0] > nome [1] :
    nome[1], nome[0] = nome[0], nome[1]
print(nome[0], nome[1])