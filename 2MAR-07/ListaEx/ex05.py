# Elabore um programa que leia do teclado o sexo de uma pessoa. Se o sexo
# digitado for "M" ou "m" ou "F" ou "f", escrever na tela "Sexo válido! ". Caso contrário,
# exibir "Sexo inválido! ".

s = input("Insira o seu gênero (f / m): ")

if s == "f" or s == "F":
    print("Fêminino")
elif s == "m" or s =="M" :
    print("Masculino")
else :
    print("Comando inválido!")
