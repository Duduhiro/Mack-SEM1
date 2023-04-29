""" Elabore um programa que leia do teclado o sexo de uma pessoa. Se o sexo digitado for "M" ou "m"
ou "F" ou "f", escrever na tela "Sexo válido! ". Caso contrário, exibir "Sexo inválido! ". """

sexo = input("Sexo: ")

if sexo.lower() == "m" or sexo.lower() == "f" :
    print("Sexo válido!")
else: 
    print("Sexo inválido!")