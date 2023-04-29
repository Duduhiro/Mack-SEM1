""" Implemente um programa que ajude o DETRAN a saber, o total de recursos que foram arrecadados
com a aplicação de multas de trânsito. O algoritmo deve ler as seguintes informações para cada
motorista:
• O número da carteira de motorista (de 1 a 9999);
• Número de multas;
• Valor de cada uma das multas.
Deve ser impresso o valor da dívida de cada motorista e ao final da leitura o total de recursos
arrecadados (somatório de todas as multas). O algoritmo deverá imprimir também o número da
carteira do motorista que obteve o maior número de multas. O programa termina quando o usuário
digitar -1 no número da carteira do motorista. """


multas = []
maxMulta = 0
maxMultado = 0

while True : 
    devendo = 0
    nCarteira = int(input("N° Carteira: "))
    if nCarteira == -1 :
        break
    nMultas = int(input("N° Multas: "))
    for i in range (nMultas) :
        multa = float(input(f"Insira o valor da multa {i + 1}: "))
        multas.append(multa)
        devendo += multa
    print(f"Você está devendo {devendo:.2f}")
    if nMultas > maxMulta :
        maxMulta = nMultas
        maxMultado = nCarteira
print(f"Foi arrecadado um total de R${sum(multas):.2f} em multas")
print(f"O maior portador de multas foi a pessoa com a carteira {maxMultado}")
