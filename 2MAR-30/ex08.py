""" Uma empresa deseja reajustar o salário de seus empregados conforme a seguinte tabela:

SALÁRIO ACRÉSCIMO
superior ou igual a 3.000,00 4,5%
inferior a 3.000,00 mas superior ou igual a 2.000,00 6,5%
inferior a 2.000,00 8,5%

Para cada empregado serão digitados os seguintes dados: nome do empregado, sexo e salário.
Obs: fazer consistência dos dados de entrada utilizando Estrutura de Repetição (sexo – aceitar
somente "F" ou "M"; salário – aceitar a partir de 850,00). Elabore um programa que leia a
quantidade de empregados e em seguida o conjunto de dados de cada empregado, calcule e
escreva:
 """

nEmployee = int(input("Insira a quantidade de funcionários: "))

result = "  NOME  | GÊNERO | SALÁRIO\n"
while nEmployee < 1 : 
    nEmployee = int(input("Valor inválido. Insira outro valor: "))

fem = 0
masc = 0
salarioMeio = 0
salarioMasc = 0

for i in range (nEmployee) :
    name = input("Insira o nome do %i° funcionário: " %(i + 1))
    gender = input("Insira o gênero da/do %s (f/m): " %(name))
    paycheck = float(input("Insira o salário do funcionário %s: " %(name)))

    if paycheck >= 3000 :
        paycheck *= 1.045
    elif paycheck >= 2000 :
        paycheck *= 1.065
        salarioMeio += 1
    else :
        paycheck *= 1.085

    if gender == "f" :
        fem += 1
        result += name + " | feminino | " + str(paycheck) + "\n"
    else :
        masc += 1
        salarioMasc += paycheck
        result += name + " | masculino | " + str(paycheck) + "\n"

print(result)
print()
print("%i funcionários receberam aumento de 6,5" %(salarioMeio) + "%")
print("O salário reajustado médio do sexo masculino é de %.2f" %(salarioMasc / masc))
print("O percentual de empregados do sexo feminino entre o total de empregados é de %.1f" %((fem /(fem + masc)) * 100) + "%")