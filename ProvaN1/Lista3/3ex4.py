""" Faça um programa em C que calcule e apresente quanto deve ser pago por um produto
considerando a leitura do preço de etiqueta (PE) e o código da condição de pagamento (CP). Utilize
para os cálculos a tabela de condições de pagamento a seguir:
1 À vista em dinheiro ou cheque, com 10% de desconto
2 À vista com cartão de crédito, com 5% de desconto
3 Em 2 vezes, preço normal de etiqueta sem juros
4 Em 3 vezes, preço de etiqueta com acréscimo de 10
 """
preco = float(input("Preço do produto: "))
cp = int(input("Condição de pagamento (1-4): "))
if cp == 1 :
    print(f"Valor a ser pago: R${preco * 0.9}")
elif cp == 2 :
    print(f"Valor a ser pago: R${preco * 0.95}")
elif cp == 3 :
    print(f"Valor a ser pago: R${preco}")
else :
    print(f"Valor a ser pago: {preco * 1.1}")