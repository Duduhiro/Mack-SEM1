""" 10) Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule 
e mostre o valor do aumento e o novo salário. """

salario = float(input("Salário: "))
aumento = int(input("Aumento (0 - 100%): "))
print(f'Novo salário: {salario + (salario * (aumento / 100)):.2f}')