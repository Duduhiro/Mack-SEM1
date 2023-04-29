# Crie um programa que apresente na tela um menu de opções
# com o nome dos pratos que são servidos por um restaurante, tal
# como é ilustrado ao lado.
# Após a apresentar as opções, leia a escolha do usuário e mostre
# qual foi o prato selecionado ou a informação de a opção feita
# não é inválida.

print(".:: Menu do dia ::.\n" +
      "1. Virado a paulista\n" +
      "2. Bife a rolê\n" +
      "3. Feijoada\n" +
      "4. Macarrão com frango\n" +
      "5. Filé de peixe")

n = int(input("Qual seria a sua escolha do dia? "))

while n < 1 or n > 5 :
    n = int(input("Escolha inválida. Qual seria a sua escolha? "))

if n == 1 :
    print("Excelente escolha! Um Virada paulista")
elif n == 2 :
    print("Excelente escolha! Um Bife a rolê")
elif n == 3 :
    print("Excelente escolha! Uma Feijoada")
elif n == 4 :
    print("Excelente escolha! Um Macarrão com frango")
else :
    print("Excelente escolha! Um Filé com peixe")