# 4. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print("----------- PAYCHECK CALCULATOR -----------")
vhora = float(input("Insira o quanto você ganha por hora: "))
horas = float(input("Insira a quantidade de horas trabalhadas: "))
print("O seu salário desse mês foi de: %.2f" %(vhora * horas))