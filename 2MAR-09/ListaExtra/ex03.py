# Diante de mudanças climáticas e recorrentes crises hídricas, as pessoas de uma certa região
# decidiram construir reservatórios para armazenar água em suas propriedades. Desenvolva um script
# Python que auxilie os utilizadores do reservatório a controlarem seu consumo.
# Assim, colete do teclado as dimensões de um reservatório (altura, largura e comprimento, em
# centímetros) e o consumo médio diário dos utilizadores do reservatório (em litros/dia).
# Considerando que o reservatório esteja cheio e tenha formato cúbico, informe:
# a) A capacidade total do reservatório, em litros;
# b) A autonomia do reservatório, em dias;
# c) A classificação do consumo, de acordo com a quantidade de dias de autonomia:
# • Consumo elevado, se a autonomia for menor que 2 dias;
# • Consumo moderado, se a autonomia estiver entre 2 e 7 dias;
# • Consumo reduzido, se a autonomia maior que 7 dias.
# Obs.: Considere que 1 litro equivale a 10 cm3
import math

medida = float(input("Insira a medida de um lado do reservatório (em cm): "))
consumo = int(input("Insira o consumo diário: "))
medida = math.pow(medida, 3) / 10
consumo = medida / consumo 
print("A medida do seu reservatório é de: %.2f cm²" %(medida))
print("O reservatório cheio irá durar, em média, %.0f dias" %(consumo))
if consumo < 2 :
    print("O consumo da região é elevado")
elif consumo >= 2 and consumo <= 7 :
    print("O consumo da região é moderado")
else :
    print("O consumo da região é reduzido")
