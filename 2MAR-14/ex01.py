""" Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente.
A tabela de preços do hospital é a seguinte:
 Quartos:
o particular – R$ 360,00
o semi-particular – R$ 210,00
o coletivo – R$ 185,00
 WIFI: R$ 3,00
 TV a cabo: R$ 4,00
Escreva um programa que leia:
 o número de dias gastos no hospital;
 o tipo de quarto;
 se usou ou não o WIFI (Sim ou Nao);
 se usou ou não a TV a cabo (Sim ou Nao).
Ao final, emita um relatório, como o exemplo, a seguir:
Número de dias no hospital: 5
Tipo de quarto: ..................... Particular
Diárias: .................................. 1800,00
WIFI: ..................................... 3,00
TV a cabo: ............................ 4,00
Total: ………………………….. 1807,00
"""

print("------------- Calculadora de gastos de um paciente -------------")

dia = int(input("Quantos dias o paciênte ficou no hospital: "))
tipo = int(input("Qual foi o tipo de quarto escolhido? 1- Particular | 2- Semi-Particular | 3- Coletivo\n"))
wifi = int(input("Foi usado WI-FI? 1- Sim | 2- Não\n"))
tv = int(input("Foi usado a TV? 1- Sim | 2- Não\n"))

if tipo == 1 : 
    dia = dia * 360
    print("Tipo de quarto: ..................... Particular")
    print("Diárias:  .............................. %.2f" %(dia))
    total = dia
elif tipo == 2 :
    dia = dia * 210
    print("Tipo de quarto: ................ Semi-Particular")
    print("Diárias:  .............................. %.2f" %(dia))
    total = dia
else :
    dia = dia * 185
    print("Tipo de quarto: ...................... Coletivo")
    print("Diárias:  .............................. %.2f" %(dia))
    total = dia

if wifi == 1 and tv == 1 :
    total += 7
    print("WIFI: ..................................... 3,00")
    print("TV a cabo: ................................ 4,00")
elif wifi == 0 and tv == 1 :
    total += 4
    print("WIFI: ..................................... 0,00")
    print("TV a cabo: ................................ 4,00")
elif wifi == 1 and tv == 0 :
    total += 3
    print("WIFI: ..................................... 3,00")
    print("TV a cabo: ................................ 0,00")
else :
    print("WIFI: ..................................... 0,00")
    print("TV a cabo: ................................ 0,00")

print("Total: ………………………….. %.2f" %(total))