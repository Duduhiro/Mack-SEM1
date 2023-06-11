""" 8) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a 
pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. """

km = int(input('Km percorrido: '))
dias_alugados = int(input("Dias alugados: "))
print(f'Preço total: {(60 * dias_alugados) + (.15 * km):.2f}')