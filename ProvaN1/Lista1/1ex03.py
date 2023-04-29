""" Sabe-se que o valor de cada 1000 litros de água corresponde a 2% do salário mínimo. Elabore um
programa que receba o valor do salário mínimo e a quantidade de água consumida em uma
residência por mês. Calcule e mostre:
a) O valor da conta de água.
b) O valor a ser pago com desconto de 15%. """

salario = float(input("Insira o salário mínimo: "))
consumo = float(input("Insira a quantidade de água consumida em 1 mês: "))

conta = ((salario / 50) / 1000) * consumo
print(f"O valor da conta será de {consumo:.2f}. Com o desconto de 15% será de {consumo * 0.85:.2f}")