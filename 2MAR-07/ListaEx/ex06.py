# Dado o preço de um produto (inteiro), elabore um programa que calcule e apresente 
# a menor quantidade de notas (de cada valor) necessárias para efetuar o pagamento da compra desse produto.

# Só apresente as notas que serão utilizadas, ou seja, se para pagar o valor você 
# não utilizar a nota de 5, ela não deverá ser apresentada.

# Considere como valores de notas: 1, 2, 5, 10, 20, 50, 100.

print("Essa é um programa que calcula a quantidade de notas necessária para comprar um produto")
price = int(input("Insira o valor do produto: "))
stop = False
result = "O total de notas necessário é: "
cem = 0
cinq = 0
vin = 0
dez = 0
cinc = 0
doi = 0
um = 0

while stop == False:
    if price >= 100:
        price -= 100
        cem += 1
    elif price >= 50:
        price -= 50
        cinq += 1
    elif price >= 20:
        price -= 20
        vin += 1
    elif price >= 10:
        price -= 10
        dez += 1
    elif price >= 5: 
        price -= 5
        cinc += 1
    elif price >= 2:
        price -= 2
        doi += 1
    elif price >= 1:
        price -= 1
        um += 1
    else: 
        stop = True

if cem > 0:
    result = result + str(cem) + " nota(s) de 100 | "
if cinq > 0:
    result = result + str(cinq) + " nota(s) de 50 | "
if vin > 0:
    result = result + str(vin) + " nota(s) de 20 | "
if dez > 0:
    result = result + str(dez) + " nota(s) de 10 | "
if cinc > 0:
    result = result + str(cinc) + " nota(s) de 5 | "
if doi > 0:
    result = result + str(doi) + " nota(s) de 2 | "
if um > 0:
    result = result + str(um) + " nota(s) de 1 | "

print("\n" + result + "\n")
