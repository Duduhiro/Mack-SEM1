"""
Instituto Presbiteriano Mackenzie - FCI - Turma 01J12 - BSI
Eduardo Hiroyuki Tamaributi
Isabelle Ramos Miranda
Weikai Xia
"""

""" Em algumas engines é muito comum transladar a origem das coordenadas e que, por conseguinte, deslocam
também os quadrantes. Um dos objetivos desse trabalho é escrever um programa que a partir da origem
translada (X,Y) do sistema de coordenadas cartesianas e uma quantidade determinada de pontos, informa
para cada ponto qual é o seu quadrante transladado e quantos pontos estão em cada quadrante.
A entrada de dados ao programa é realizada através do teclado, atendendo a seguinte configuração:
• No início do programa são lidos dois números inteiros, X e Y, representando as coordenadas da origem
transladada.
• Depois é informado um inteiro N indicando a quantidade de pontos que deverão ser lidos e
processados pelo programa.
• Em seguida, serão lidos os valores das coordenadas dos N pontos pelo programa.
Para cada ponto lido o programa deve informar, imprimindo no console, a qual quadrante translado o ponto
pertence. Caso o ponto esteja na abscissa transladada ou ordenada transladada o programa imprimirá “sobre
o eixo de coordenadas”. """

# Parte A - Trabalho N1 

print("---------- Parte A ----------")
oX = int(input("Insira a coordenada X da origem transladada: ")) # Faz o input da coordenada X da origem transladada  
oY = int(input("Insira a coordenada Y da origem transladada: ")) # Faz o input da coordenada Y da origem transladada 

n = int(input("Insira a quantidade de pontos que serão lidos: ")) # Faz o input da quantidade de pontos que serão lidos e processados 

for i in range (n) :
    pX = int(input("Insira a coordenada X do ponto %i: " %(i + 1))) # Faz o input da coordenada X do ponto i 
    pY = int(input("Insira a coordenada Y do ponto %i: " %(i + 1))) # Faz o input da coordenada Y do ponto i 
    if pX == oX or pY == oY: # Confere se o ponto i está sobre o eixo de coordenadas                                        
        print("Ponto (%i, %i) está sobre o eixo de coordenadas" %(pX, pY))                        
    else :
        if pX > oX and pY > oY :
            print("Ponto (%i, %i) está no 1° quadrante" %(pX, pY)) # Verifica se o ponto p está no primeiro quadrante 
        elif pX < oX and pY > oY :
            print("Ponto (%i, %i) está no 2° quadrante" %(pX, pY)) # Verifica se o ponto p está no segundo quadrante 
        elif pX < oX and pY < oY :
            print("Ponto (%i, %i) está no 3° quadrante" %(pX, pY)) # Verifica se o ponto p está no terceiro quadrante 
        else :
            print("Ponto (%i, %i) está no 4° quadrante" %(pX, pY)) # Printa que o ponto p está no quarto quadrante 

""" 
O gráfico abaixo ilustra o início do deslocamento de um robô que parte do ponto A (2, 0), movimentando-se
para cima ou para a direita, com velocidade de uma unidade de comprimento por segundo, no plano
cartesiano. Observe que é um movimento programado: uma unidade para cima, duas para direita, uma para
cima, duas para direita e assim sucessivamente. 

Após seu programa imprimir as informações da Parte A, ele irá pedir ao usuário que informe a coordenada de
origem do robô (ponto A) e por quanto tempo ele irá caminhar. Com esses dados, seu programa deverá
imprimir qual será sua coordenada final no plano cartesiano. Considerar o plano cartesiano normal, com
origem (0, 0).
 """

# Parte B - Trabalho N1 

print("\n---------- Parte B ----------")
aX = int(input("Insira a coordenada X do ponto de origem A do robô: ")) # Faz o input da coordenada X onde o robô vai começar 
aY = int(input("Insira a coordenada Y do ponto de origem A do robô: ")) # Faz o input da coordenada Y onde o robô vai começar 
n = int(input("Insira por quanto tempo o robô irá caminhar: "))         # Faz o input de quanto tempo o robô irá caminhar 
i = 0
lado = False
while i < n : 
    if lado == False :  # Caso a variável lado estiver falsa, o robô irá caminhar para cima 
        aY += 1         # Faz o robô caminhar uma casa para cima 
        i += 1          # Adiciona 1 a variavel que está controlando o tempo de caminhada do robô 
        lado = True     # Define a variavel de direção como verdadeira, para o robô andar para o lado na próxima leitura 
    else :              # Caso a variável lado estiver verdadeira, o robô irá caminhar para o lado 
        aX += 1         # Faz o robô caminhar 1 casa para a direita 
        i += 1          # Adiciona 1 a variavel que está controlando o tempo de caminhada do robô 
        if i >= n :
            break       # Se depois do primeiro passo para a direita, i alcançar n, o loop para 
        aX += 1         # Faz o robô caminhar 1 casa para a direita 
        i += 1          # Adiciona 1 a variavel que está controlando o tempo de caminhada do robô 
        lado = False    # Define a variavel de direção como falsa, para o robô andar para cima na próxima leitura e
print("Ao final da caminhada, o robô estará no ponto (%i, %i) do plano cartesiano" %(aX, aY)) # Printa o reultado da movimentação do robô 