""" Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de altura e sexo (0
= masc, 1 = fem) das pessoas. Faça um programa que leia os dados dos habitantes e informe:
• a maior e a menor altura encontradas;
• a média de altura das mulheres;
• a média de altura da população;
• o percentual de homens na população.
O programa termina quando o usuário digitar -1 para o sexo. """
sexo = 0
homem = mulher = altMul = altHom = max = 0
min = 300

while sexo != -1 :
    sexo = int(input("Insira o gênero da pessoa (0- Masc / 1- Fem): "))
    if sexo == -1 :
        break
    altura = int(input("Insira a altura em cm: "))

    if altura > max :
        max = altura
    if altura < min :
        min = altura

    if sexo == 0: 
        altHom += altura
        homem += 1
    else :
        altMul += altura
        mulher += 1
    
print("A maior altura é %icm e a menor altura é %icm" %(max, min))
print("A média de altura entre as mulheres é de %icm" %(altMul / mulher))
print("A média de altura total da população é de %icm" %((altMul + altHom) / (mulher + homem)))
print("O percentual de homens na população é de %i" %(homem / (homem + mulher) * 100) + "%")