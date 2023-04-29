""" Elabore um programa que mostre o preço de etiqueta de um produto e calcule e mostre o quanto
deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de
pagamento.
Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o cálculo
adequado.
Código Condições de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 5% de desconto
3 Em 2 vezes, preço normal de etiqueta sem juros
4 Em 3 vezes, preço normal de etiqueta mais juros de 10% """

price = float(input("Insira o preço do produto: "))
tipo = int(input("Insira o tipo de pagamento\n"
                 + "1 À vista em dinheiro ou cheque, recebe 10% de desconto\n"
                 + "2 À vista no cartão de crédito, recebe 5% de desconto\n"
                 + "3 Em 2 vezes, preço normal de etiqueta sem juros\n"
                 + "4 Em 3 vezes, preço normal de etiqueta mais juros de 10%\n"))
if tipo == 1 :
    print("O valor a ser pago será de: R$%.2f" %(price * 0.9))
elif tipo == 2 :
    print("O valor a ser pago será de: R$%.2f" %(price * 0.95))
elif tipo == 3 :
    print("O valor a ser pago será de: R$%.2f" %(price))
else :
    "O valor a ser pago será de: R$%.2f" %(price * 1.1)