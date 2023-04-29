""" Faça um programa que tendo como dados de entrada o código de região de localização do cliente,
o nome do cliente, o número de peças vendidas e o nome do vendedor; calcule e informe o valor do
frete, a comissão do vendedor e o lucro obtido com a venda, sabendo-se que:
 O valor do frete depende da quantidade transportada e da região;
 Custo por peça = R$ 7,00;
 Custo total = custo por peça * número de peças vendidas;
 Valor total da venda = custo total acrescido de 50%;
 Comissão do vendedor = 6,5 % do valor total da venda;
 Lucro = Valor total venda – custo total – comissão do vendedor;
Código da Região | Nome da Região | Valor do frete por peça (até 1.000 peças)R$ | Valor do frete por peça (acima de 1.000 peças) R$
1                       Sul                            1,00                                              0,9
2                      Norte                           1,10                                              1,0
3                      Leste                           1,15                                              1,10
4                      Oeste                           1,20                                              1,15 """

region = int(input("Insira o código da região: 1- Sul | 2- Norte | 3- Leste | 4- Oeste "))
name = input("Insira o seu nome: ")
q = int(input("Insira a quantidade de peças vendidas: "))

custo = q * 7
if region == 1: 
    if q <= 1000 :
        frete = 1 * q
    else :
        frete = 0.9 * q
elif region == 2:
    if q <= 1000 :
        frete = 1.1 * q
    else :
        frete = 1 * q
elif region == 3: 
    if q <= 1000 :
        frete = 1.15 * q
    else :
        frete = 1.1 * q
else :
    if q <= 1000 :
        frete = 1.2 * q
    else :
        frete = 1.15 * q

total = custo * 1.5
comissao = total * 0.065
lucro = total - comissao - custo
print("Frete....................... %.2f" %(frete))
print("Comissão do vendedor........ %.2f" %(comissao))
print("Lucro....................... %.2f" %(lucro))