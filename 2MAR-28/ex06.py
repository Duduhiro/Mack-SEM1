# Faça um programa que solicite 10 números inteiros entre 1 a 10 e apresenta a média aritmética
# entre eles. O programa deverá fazer uma validação de forma que o usuário obrigatoriamente
# somente digite números neste intervalo.

media = 0 
for i in range (10) :
    n = int(input("Insira um número: "))
    while n < 1 or n > 10 : 
        n = int(input("Valor incorreto (1 - 10). Insira o valor novamente: "))
    media += n

print("A média aritmética é de: %.1f" %(media / 10))