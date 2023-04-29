# 5. Faça um programa que calcule e mostre o IMC (índice de massa corporal) de uma pessoa, considerando
# que ela irá dizer qual o seu peso e qual a sua altura ( imc = peso/(altura*altura) ).

print("----------- IMC CALCULATOR -----------")
peso = float(input("Insira o seu peso (em KG): "))
altura = float(input("Insira a sua altura (Ex: 1.75): "))
imc = peso / (altura * altura)
print("O seu IMC é de: %.2f" %(imc))
print("Um IMC ideal está entre 18.5 e 24.9\n\n\n")
