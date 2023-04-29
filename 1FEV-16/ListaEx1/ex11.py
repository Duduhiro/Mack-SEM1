import math
size = float(input("Insira o tamanho do terreno a ser pintado: "))
quant = size / 54
quant = math.ceil(quant)
print("Serão necessárias %.0f latas de tinta" %(quant), "e o valor será de: $%.2f" %(quant * 80))

