""" João tem 1,50m e cresce 2 centímetros por ano, enquanto Jussara tem 1,10m e cresce 3 centímetros
por ano. Faça um programa que calcule e imprima quantos anos serão necessários para que Jussara
seja maior que João. """

jo = 1.50
ju = 1.10
counter = 0

while jo > ju :
    jo += 0.02
    ju += 0.03
    counter += 1
print("Serão necessários %i anos" %(counter))