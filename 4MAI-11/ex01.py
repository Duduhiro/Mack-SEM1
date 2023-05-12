""" Faça um programa que permita ao usuário digitar o seu nome e em
seguida mostre o nome do usuário das seguintes formas:
a) De trás para frente exibindo as letras em maiúsculo (Obs: o usuário
pode digitar tanto letras maiúsculas quanto minúsculas). """

nome = input("Nome: ")
nome = nome.upper()
print(nome[::-1])

"""b) Na vertical"""

for i in nome :
    print(i)

"""c) Na vertical em escada"""

text = ""
for i in nome :
    text += i
    print(text)

"""d) Na vertical em escada invertida"""
text = [x for x in nome]
i = len(text) - 1
while i != -1 :
    print("".join(text))
    text.pop(i)
    i -= 1