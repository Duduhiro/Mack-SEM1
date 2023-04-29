""" Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. """

km = int(input("Km: "))
dias = int(input("Dias: "))
preco = (dias * 60) + (0.15 * km)
print(f"O aluguel foi R${preco:.2f}")