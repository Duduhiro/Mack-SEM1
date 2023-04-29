""" Um dos jogos de nossa infância é jogo de Joquempô no qual cada criança escolhe entre:
PEDRA, PAPEL E TESOURA.
Como jogar: Dois participantes ficam um de frente para o outro e, ao mesmo tempo, jogam uma
das mãos para frente representando um dos três símbolos: pedra (mão fechada), papel (mão
aberta) ou tesoura (dedos indicador e médio estendidos).
Para definir o vencedor segue-se as seguintes regras:
1) pedra ‘quebra’ a tesoura; 2)
tesoura ‘corta’ o papel;
3) papel ‘embrulha’ a pedra.
4) Se ambas escolhem a mesma opção, ocorre um empate.
Sabendo agora como funciona o jogo, crie um programa que joguem: um usuário (teclado) e uma
máquina (computador).
Crie uma variável para cada jogador que deve armazenar a opção escolhida (pedra, papel ou
tesoura) do jogador.
Outra variável será a jogada do computador que deverá ser escolhida a opção de forma aleatória
entre três opções (pedra, papel ou tesoura).
Dica, poderá ser utilizado a biblioteca random, função “random.choice” para escolha entre
'pedra', 'tesoura' e 'papel'.
Ao final é apresentado a jogada do computador, o ganhador e a jogada (regra) realizada.
 """
import random

game = ["pedra", "papel", "tesoura"]
player = input("Pedra, papel ou tesoura? ")
bot = random.choice(game)

if player == bot :
    print("Empate")
else :
    if player == "papel" and bot == "pedra" :
        print("Ganhou, o bot escolheu %s" %(bot))
    elif player == "papel" and bot == "tesoura" :
        print("Perdeu, o bot escolheu %s" %(bot))
    elif player == "tesoura" and bot == "pedra" :
        print("Perdeu, o bot escolheu %s" %(bot))
    elif player == "tesoura" and bot == "papel" :
        print("Ganhou, o bot escolheu %s" %(bot))
    elif player == "pedra" and bot == "papel" :
        print("Perdeu, o bot escolheu %s" %(bot))
    elif player == "pedra" and bot == "tesoura" :
        print("Ganhou, o bot escolheu %s" %(bot))
