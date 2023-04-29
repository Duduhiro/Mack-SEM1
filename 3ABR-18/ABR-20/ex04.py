""" Escreva um programa em Python que receba dois números inteiros. Execute e mostre o resultado
das operações listadas, a seguir, de acordo com a escolha do usuário. O menu deve ser apresentado
enquanto o usuário não escolher a opção 0 (Sair):
1 - Soma dos dois números digitados
2 - Diferença dos dois números digitados
3 - Produto dos dois números digitados
4 - Divisão dos dois números digitados
0 - Sair
Organize o código de maneira que o programa principal fique responsável pela entrada e saída de
dados, enquanto as operações são executadas por sub-rotinas específicas, sendo:
• menu(): apresenta o menu e valida a opção que o usuário digitou, retornando a opção escolhida;
• soma(n1,n2): irá retornar a soma de n1 e n2;
• diferenca(n1,n2): irá retornar a diferença de n1-n2;
• produto(n1,n2): irá retornar a multiplicação n1 e n2;
• divisao(n1,n2): irá retornar a divisão de n1/n2 se n2 for diferente de zero.  """

def menu () :
    print('1- Soma dos dois números digitados\n' +
          '2- Diferença dos dois números digitados\n' +
          '3- Produto dos dois números digitados\n' +
          '4- Divisão dos dois números digitados\n' +
          '0- Sair')
    escolha = int(input())
    return escolha

def soma (n1, n2) :
    return n1 + n2
def diferenca (n1, n2) :
    return n1 - n2
def produto (n1, n2) :
    return n1 * n2
def divisao (n1, n2) :
    if (n2 != 0) :
        return n1 / n2

while True :
    escolha = menu()
    if escolha == 0 :
        break
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))

    if escolha == 1 :
        print(f"N1 + N2 = {soma (n1, n2)}")
    elif escolha == 2 :
        print(f"N1 - N2 = {diferenca (n1, n2)}")
    elif escolha == 3 :
        print(f"N1 * N2 = {produto (n1, n2)}")
    elif escolha == 4 :
        print(f"N1 / N2 = {divisao (n1, n2)}") 
print()