""" screva um programa em Python que:
a. Defina 3 variáveis com valores que armazenem
i. O nome de uma fruta
ii. O nome de verdura
b. O nome de um legumeMostre uma mensagem “Aqui estão os nomes de uma
fruta, uma verdura e um legume”
c. Após essa mensagem, mostre, na ordem, o nome da fruta, da verdura e do legume
Lembre-se de usar nomes válidos de variáveis e que definam o propósito do valor armazenado. """

comidas = ["Morango", "Alface", "Beringela"]
print("Aqui estão os nomes de uma fruta, verdura e legume")
for i in range (len(comidas)) :
    print(comidas[i], end=", ")