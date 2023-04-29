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

# Parte B - Trabalho N1 - Eduardo Hiroyuki Tamaributi - 32331862 - 01J12

aX = int(input("Insira a coordenada X do ponto de origem A do robô: ")) # Faz o input da coordenada X onde o robô vai começar / Input the starting X coordinate of the robot
aY = int(input("Insira a coordenada Y do ponto de origem A do robô: ")) # Faz o input da coordenada Y onde o robô vai começar / Input the starting Y coordinate of the robot
n = int(input("Insira por quanto tempo o robô irá caminhar: "))         # Faz o input de quanto tempo o robô irá caminhar / Input the duration that the robot will walk
i = 0
lado = False
while i < n : 
    if lado == False :  # Caso a variável lado estiver falsa, o robô irá caminhar para cima / If the variable "lado" is False, the robot will walk upwards
        aY += 1         # Faz o robô caminhar uma casa para cima / The robot walks 1 square upwards
        i += 1          # Adiciona 1 a variavel que está controlando o tempo de caminhada do robô / Adds 1 to the variable which controls the duration of the walk
        lado = True     # Define a variavel de direção como verdadeira, para o robô andar para o lado na próxima leitura / Defines the direction variable True
    else :              # Caso a variável lado estiver verdadeira, o robô irá caminhar para o lado / If the variable "lado" is True, the robot will walk sideways
        aX += 1         # Faz o robô caminhar 1 casa para a direita / The robot walks 1 square sideway
        i += 1          # Adiciona 1 a variavel que está controlando o tempo de caminhada do robô / Adds 1 to the variable which controls the durantion of the walk
        if i >= n :
            break       # Se depois do primeiro passo para a direita, i alcançar n, o loop para / If after the first step sideways, i reaches n, break the loop
        aX += 1         # Faz o robô caminhar 1 casa para a direita / The robot walks 1 square sideway
        i += 1          # Adiciona 1 a variavel que está controlando o tempo de caminhada do robô / Adds 1 to the variable which controls the duration of the walk
        lado = False    # Define a variavel de direção como falsa, para o robô andar para cima na próxima leitura / Define the direction variable False
print("Ao final da caminhada, o robô estará no ponto (%i, %i) do plano cartesiano" %(aX, aY)) # Printa o reultado da movimentação do robô / Prits the movement result
