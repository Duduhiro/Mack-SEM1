""" 1) Faça um programa que receba o custo de um espetáculo teatral e o preço do ingresso desse 
espetáculo. Esse programa deve calcular e mostrar:
a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo 
seja alcançado. 
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%."""

custo_espetaculo = float(input("Preço espetáculo: "))
preco_ingresso = float(input("Preço ingresso: "))
if custo_espetaculo % preco_ingresso == 0 :
    qt_vendas = custo_espetaculo // preco_ingresso
else :
    qt_vendas = custo_espetaculo // preco_ingresso + 1

print(f'Quantidade para cobrir o preço do espetáculo: {(qt_vendas):.0f}')

custo_espetaculo *= 1.23
if custo_espetaculo % preco_ingresso == 0 :
    qt_vendas = custo_espetaculo // preco_ingresso
else :
    qt_vendas = custo_espetaculo // preco_ingresso + 1
print(f'Para lucro de 23%: {(qt_vendas):.0f}')