print("Esse é um programa que calcula a média ponderada de 3 notas")
nota = 0
peso = 0
for i in range (3):
    inpNota = int(input("Insira a sua %.0fa nota: " %(i + 1)))
    inpPeso = int(input("Insira o peso dessa nota: "))
    nota = nota + (inpNota * inpPeso)
    peso = peso + inpPeso
final = nota / peso
print("Sua média ponderada é de: %.1f" %(final))