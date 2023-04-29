""" Nos cassinos de Las Vegas um jogo muito famoso é o jogo dos dados feito da seguinte forma:
“Aposte em um número que seja o resultado da soma deles !”
Ganha o jogo se acertar a aposta.
Crie um programa para lançar os 2 dados, solicitar ao usuário sua aposta e dar uma mensagem
se o jogador ganhou ou perdeu.
Crie duas variáveis para representar os dados e uma para sua aposta.
Lembre-se que uma aposta deve ser maior ou igual a 2 e menor ou igual a 12.
Dica: lembre-se de utilizar a biblioteca random para gerar um número entre 1 e 6 """

import random

d1 = random.randint(1, 7)
d2 = random.randint(1, 7)
bet = 0
while bet < 2 or bet > 12 :
    bet = int(input("Insira a sua aposta: "))

if bet == d1 + d2 :
    print("Winner Winner Chicken Dinner")
else :
    print("Quase, o resultado foi %i" %(d1 + d2))

