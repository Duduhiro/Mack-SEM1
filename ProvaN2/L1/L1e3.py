""" 3) Sabe-se que o valor de cada 1000 litros de água corresponde a 2% do salário mínimo. Elabore um 
programa que receba o valor do salário mínimo e a quantidade de água consumida em uma 
residência por mês. Calcule e mostre:
a) O valor da conta de água.
b) O valor a ser pago com desconto de 15% """

salario = float(input('Salario: '))
consumo = int(input('Consumo mensal de água: '))

valor = consumo / (500 / (salario / 100))
print(f'Valor da conta: {valor:.2f}\nValor com 15% de desconto: {valor*0.85:.2f}')