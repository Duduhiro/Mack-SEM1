valor = int(input("Insira o valor do produto: "))

result = "O total de notas necessário é: "

if valor >= 100 :
    cem = valor // 100
    valor = valor % 100
    result = result + str(cem) + " notas de 100 | "

if valor >= 50 :
    cinq = valor // 50
    valor = valor % 50
    result = result + str(cinq) + " notas de 50 | "

if valor >= 20 : 
    vin = valor // 20
    valor = valor % 20
    result = result + str(vin) + " notas de 20 | "

if valor >= 10 :
    dez = valor // 10
    valor = valor % 10
    result = result + str(dez) + " notas de 10 | "

if valor >= 5 :
    cinc = valor // 5
    valor = valor % 5
    result = result + str(cinc) + " notas de 5 | "

if valor >= 2 :
    doi = valor // 2
    valor = valor % 2
    result = result + str(doi) + " notas de 2 | "

if valor >= 1 :
    um = valor // 1
    result = result + str(um) + " notas de 1 | "

print(result)
