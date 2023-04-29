""" Faça um programa que receba o custo de um espetáculo teatral e o preço do ingresso desse
espetáculo. Esse programa deve calcular e mostrar:
a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo
seja alcançado.
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. """

custo = float(input("Insira o preço do espetáculo: "))
ingresso = float(input("Insira o preço do ingresso: "))
lucro = custo * 1.23

qIngresso = custo / ingresso
if qIngresso % 1 != 0 :
    qIngresso += 1
qLucro = lucro / ingresso
if qLucro % 1 != 0 :
    qLucro += 1

print(f"Para não haver prejuízo será necessário vender {qIngresso:.0f} ingressos. Para ter um lucro de 23% será necessário vender {qLucro:.0f} ingressos")