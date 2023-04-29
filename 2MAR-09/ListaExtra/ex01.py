# Faça um programa que receba um número inteiro e informe se ele é divisível por 10 e,
# independentemente disso, é divisível por 5; e, independentemente disso, é divisível por 2; ou se não
# é divisível por nenhum destes.

n = int(input("Insira um número: "))

if n % 10 == 0 and n % 10 == 0 and n % 10 == 0 :
    print("O número %i é divisível por 10, 5 e 2" %(n))
else :
    print("O número %i não é divisível por 10, 5 e 2" %(n))