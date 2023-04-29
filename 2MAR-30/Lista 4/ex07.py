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

carteira = max = maxCarteira = 0
while carteira != -1 :
    multas = 0
    nome = input("Insira o seu nome: ")
    carteira = int(input("Insira o número de sua carteira (1 - 9999 e -1 para sair): "))
    if carteira == -1 :
        break
    nMultas = int(input("Insira o número de multas a serem registradas: "))
    for i in range (nMultas) :
        multas += float(input("Insira o valor da multa %i: " %(i + 1)))
    if multas > max : 
        max = multas
        maxCarteira = carteira
    print("%s, portador da carteira %i, o valor total das suas multas é de: %.2f" %(nome, carteira, multas))
print("A maior somatória de multas pertence ao portador da carteira %i com o valor total de: %.2f" %(maxCarteira, max))