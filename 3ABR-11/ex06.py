""" Uma empresa deseja reajustar o salário de seus empregados conforme a seguinte tabela:

Para cada empregado serão digitados o nome do empregado e salário.
Elabore um programa que leia a quantidade de empregados e em seguida o conjunto de dados
de cada empregado – nome e salário. Calcule e mostre:
a) para cada empregado, o salário reajustado (conforme tabela);
b) a quantidade de empregados que receberam reajuste de 10%;
c) o salário médio (após o reajuste) entre os empregados; """

qEmpregado = int(input("Insira a quantidade de funcionários: "))
tabela = ""
contador = 0
total = 0 

for i in range (qEmpregado) :
    nome = input("Insira o seu nome, empregado %i: " %(i + 1))
    salario = float(input("Insira o seu salário, %s: " %(nome)))
    if salario >= 3000 :
        salario *= 1.08
    elif salario >= 2000 :
        salario *= 1.1
        contador += 1
    else : 
        salario *= 1.12
    total += salario
    tabela += nome + " | R$" + "%.2f" %(salario) + "\n"
print(tabela, end="")
print("%i receberam um aumento de 10" %(contador) + "%")
print("O salário médio é de: R$%.2f" %(total / qEmpregado))
