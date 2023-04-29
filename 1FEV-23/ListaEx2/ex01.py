#Bonificação para funcionários

#Escreva um programa que receba dois valores, sendo o primeiro
#correspondente ao salário de um funcionário e o outro ao
#percentual de aumento a ser concedido.
#Calcule o valor do aumento a ser aplicado sobre o salário,
#apresentando o valor relativo ao aumento e o novo salário.
#Exemplo: Para um salário de 2000.00 e um percentual de aumento
#de 15%, o valor do aumento será 300.00 e o novo salário passar a
#ser de 2300.00.

print("Esse é um programa que calcula a bonificação para funcionários.")
salario = float(input("Insira o seu salário: "))
aumento = float(input("Insira o percentual do seu aumento: "))
aumento = salario * (aumento / 100) 
print("O seu aumento será de: $%.2f. E o seu salário será de: $%.2f." %(aumento, salario + aumento))