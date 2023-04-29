#Conversão de escalas

#Faça um programa que peça a temperatura em graus Fahrenheit,
#transforme e mostre a temperatura em graus Celsius

print("Esse é um programa que transforma a temperatura de Fahrenheit para Celsius")
temp = float(input("Insira a temperatura (em °F): "))
temp = (temp - 32) * 5 / 9
print("A temperatura convertida para Celsius é de: %.1f°C" %(temp))