""" João tem 1,50m e cresce 2 centímetros por ano, enquanto Jussara tem 1,10m e cresce 3 centímetros
por ano. Faça um programa que calcule e imprima quantos anos serão necessários para que Jussara
seja maior que João. """

joao = 1.50
jussara = 1.1
count = 0

while jussara < joao :
    count += 1
    jussara += 0.03
    joao += 0.02
print(f"Será necessário {count} anos para Jussara alcançar João")