#Identidade trigonométrica

#Faça um programa codifique as dois lados da equação abaixo,
#calculando-os separadamente e apresente ambos os resultados de
#modo a permitir que o usuário comprove que esta identidade
#trigonométrica é verdadeira para quaisquer dois ângulos 𝛼 e 𝛽:

import math

alpha = int(input("Insira o ângulo alpha: "))
beta = int(input("Insira o ângulo beta: "))

a = math.cos(alpha) + math.cos(beta)
b = 2 * math.cos(1 / 2) * (alpha + beta) * math.cos(1 / 2) * (alpha - beta)

print("O lado esquerdo da equação deu: %f. E o lado direto da equação deu: %f." %(a,b))