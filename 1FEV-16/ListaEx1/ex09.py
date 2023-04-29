km = float(input("Insira quantos KM foram rodados: "))
dias = int(input("Insira por quantos dias o carro foi alugado: "))
price = (dias * 60) + (0.15 * km)
print("O preço total a pagar é de: $%.2f" %(price))