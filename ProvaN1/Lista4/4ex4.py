""" Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de altura e sexo (0
= masc, 1 = fem) das pessoas. Faça um programa que leia os dados dos habitantes e informe:
• a maior e a menor altura encontradas;
• a média de altura das mulheres;
• a média de altura da população;
• o percentual de homens na população.
O programa termina quando o usuário digitar -1 para o sexo."""

listAltura = []
sexo = alturaM = alturaF = hom = mul = 0
while True :
    sexo = int(input("Sexo (0- Masc | 1- Fem | -1- Sair): "))
    if sexo == -1 :
        break
    altura = float(input("Altura: "))
    listAltura.append(altura)
    if sexo == 0 :
        alturaM += altura
        hom += 1
    else :
        alturaF += altura
        mul += 1
list.sort(listAltura)
print(f"A maior altura é {listAltura[hom + mul - 1]:.2f} e a menor altura é {listAltura[0]:.2f}")
print(f"A média de altura das mulheres é {alturaF / mul:.2f}")
print(f"A média de altura da população é {(alturaM + alturaF) / (mul + hom):.2f}")
print(f"O percentual de homens na população é de {hom / (hom + mul) * 100}%")