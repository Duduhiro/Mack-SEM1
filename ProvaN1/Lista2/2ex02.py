""" Dado o preço de um produto (valor inteiro), elabore um programa que calcule e apresente a
menor quantidade de notas, de cada valor, necessárias para efetuar o pagamento da compra
desse produto.
Considere que nessa moeda há notas com os seguintes valores: 1, 2, 5, 10, 20, 50, 100. """

preco = int(input("Preço: "))

if preco >= 100 :
    print(f"Notas de 100: {preco // 100}") 
    preco = preco % 100

if preco >= 50 :
    print(f"Notas de 50: {preco // 50}")
    preco = preco % 50
if preco >= 20 :
    print(f"Notas de 20: {preco // 20}")
    preco = preco % 20
if preco >= 10 :
    print(f"Notas de 10: {preco // 10}")
    preco = preco % 10
if preco >= 5 :
    print(f"Notas de 5: {preco // 5}")
    preco = preco % 5
if preco >= 2 :
    print(f"Notas de 2: {preco // 2}")
    preco = preco % 2
if preco >= 1 :
    print(f"Notas de 1: {preco // 1}")
    preco = preco % 1
