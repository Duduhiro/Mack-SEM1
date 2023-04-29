salario = float(input("Insira o seu salário: "))
aumento = float(input("Insira a porcentagem do seu aumento (Não é necessário usar o símbolo %): "))
aumento = salario * (aumento / 100)
print("Você está recebendo um aumento de: $%.2f" %(aumento), "| E o seu novo salário será de: $%.2f" %(salario + aumento))