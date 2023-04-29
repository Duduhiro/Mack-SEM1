""" Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule
e mostre o valor do aumento e o novo salário. """

salario = float(input("Salário: "))
pAumento = float(input("Percentual de aumento: "))
salario *= 1 + (pAumento / 100)
print(f"Salário reajustado {salario:.2f}")