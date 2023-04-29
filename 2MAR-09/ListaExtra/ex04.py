# Faça um programa em C que calcule e apresente quanto deve ser pago por um produto
# considerando a leitura do preço de etiqueta (PE) e o código da condição de pagamento (CP). Utilize
# para os cálculos a tabela de condições de pagamento a seguir:

pe = float(input("Insira o preço do produto: "))
cp = int(input("Insira o código do produto (1 - 4): "))

if cp == 1 :
    print("O preço do produto será de: %.2f" %(pe * 0.9))
elif cp == 2 :
    print("O preço do produto será de: %.2f" %(pe * 0.95))
elif cp == 3 :
    print("O preço do produto será de: %.2f" %(pe))
else :
    print("O preço do produto será de: %.2f" %(pe * 1.1))