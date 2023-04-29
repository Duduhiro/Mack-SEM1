salMin = float(input("Insira o valor do salário minimo: "))
agua = float(input("Insira o gasto de água mensal: "))
salMin = salMin * 0.02
agua = agua / 1000
conta = agua * salMin
print("O valor da sua conta de água foi de: %.2f" %(conta))
desconto = conta * 0.85
print("O valor com desconto de 15%" , "será de: %.2f" %(desconto))

