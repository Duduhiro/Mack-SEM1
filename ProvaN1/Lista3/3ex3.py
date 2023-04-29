""" Diante de mudanças climáticas e recorrentes crises hídricas, as pessoas de uma certa região
decidiram construir reservatórios para armazenar água em suas propriedades. Desenvolva um script
Python que auxilie os utilizadores do reservatório a controlarem seu consumo.
Assim, colete do teclado as dimensões de um reservatório (altura, largura e comprimento, em
centímetros) e o consumo médio diário dos utilizadores do reservatório (em litros/dia).
Considerando que o reservatório esteja cheio e tenha formato cúbico, informe:
a) A capacidade total do reservatório, em litros;
b) A autonomia do reservatório, em dias;
c) A classificação do consumo, de acordo com a quantidade de dias de autonomia:
• Consumo elevado, se a autonomia for menor que 2 dias;
• Consumo moderado, se a autonomia estiver entre 2 e 7 dias;
• Consumo reduzido, se a autonomia maior que 7 dias.
Obs.: Considere que 1 litro equivale a 10 cm3. """
altura = int(input("Altura do reservatório: "))
largura = int(input("Largura do reservatório: "))
comprimento = int(input("Comprimento do reservatório: "))
consumo = int(input("Consumo (L/dia): "))
volume = altura * largura * comprimento
capacidade = volume / 1000
print(f"A capacidade total do reservatório é de {capacidade} litros")
print(f"Considerando que são gastos {consumo} litros de água por dia, a autonomia do reservatório é de {capacidade / consumo} dias")
if capacidade / consumo < 2 :
    print("Consumo elevado")
elif capacidade / consumo >= 2 and capacidade / consumo <= 7 :
    print("Consumo moderado")
else :
    print("Consumo reduzido")