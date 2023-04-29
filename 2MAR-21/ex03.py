""" O Jogo de par ou ímpar é usado onde duas pessoas jogam geralmente para decidir sobre um
impasse.
Cada pessoa escolhe entre par e a outra será o ímpar e mostra-se os dedos de sua aposta como
número.
Se a soma dos dedos entre as duas pessoas resultar em um número par ou ímpar, o ganhador é
aquele que acertou de forma correta.
Aqui faremos a suposição que uma das pessoas será o usuário (fornece o número pelo teclado) e
a outra uma máquina (gera um número aleatório).
Assim, a máquina faz a sua aposta a partir da geração de um número randômico entre 0 e 5 e o
usuário digitando via teclado.
O usuário sempre fornece a quantidade de dedos da jogada e a opção entre par ou ímpar,
portanto, a máquina será a outra opção.
Ao final o software diz quem ganhou e quantos dedos a máquina colocou. """

import random

select = int(input("1 - par / 2 - impar : "))
bet = int(input("Qual a sua aposta? "))
bot = random.randint(0, 6)
if select == 1 :
    if (bet + bot) % 2 == 0 :
        print("Ganhou")
    else :
        print("Perdeu")
else :
    if (bet + bot) % 2 == 0:
        print("Perdeu")
    else :
        print("Ganhou")
print("O número jogado pelo bot foi %i" %(bot))