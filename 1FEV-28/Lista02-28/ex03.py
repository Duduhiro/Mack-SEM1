# 3. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o
# usuário (area = lado*lado).

print("----------- SQR AREA CALCULATOR -----------")
lado = float(input("Insira a medida do lado do quadrado: "))
lado = lado * lado
print("A medida do dobro da área desse quadrado equivale a: %.2f" %(lado * 2))