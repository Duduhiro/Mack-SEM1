""" Crie um programa que apresente na tela um menu de opções
com o nome dos pratos que são servidos por um restaurante, tal
como é ilustrado ao lado.
Após a apresentar as opções, leia a escolha do usuário e mostre
qual foi o prato selecionado ou a informação de a opção feita
não é inválida.

.:: Menu do dia ::.
1. Virado a paulista
2. Bife a rolê
3. Feijoada
4. Macarrão com frango
5. Filé de peixe """

print(".:: Menu do dia ::.\n1. Virado a paulista\n2. Bife a rolê\n" +
      "3. Feijoada\n4. Macarrão com frango\n5. Filé de peixe")
menu = ["Virado a paulista", "Bife a rolê", "Feijoada", "Macarrão com frango", "Filé de peixe"]
escolha = int(input("Qual sua escolha: "))
print(f"Saindo um(a) {menu[escolha - 1]}")