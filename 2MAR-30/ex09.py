""" Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de
código. Os códigos utilizados são:
• 1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar um menu texto com as
opções ex: 1 – Jose 2- João ... etc)
• 5 - Voto Nulo
• 6 - Voto em Branco
Faça um programa que peça a quantidade de eleitores, leia os votos, calcule e mostre:
a) O total de votos para cada candidato;
b) O total de votos nulos;
c) O total de votos em branco;
d) A percentagem de votos nulos sobre o total de votos;
e) A percentagem de votos em branco sobre o total de votos """

candidatos = ["Severus" , "Albus" , "Minerva" , "Tom"]

print("----- ELEIÇÃO HOGWARTS -----\nCANDIDATOS:")
for i in range (4) :
    print("%i- %s" %(i + 1, candidatos[i]))
print("5- Voto Nulo\n6- Voto em Branco (Direcionado para quem possuir mais votos)")

maxVoters = int(input("Insira a quantidade de eleitores: "))

while maxVoters < 1 :
    maxVoters = int(input("Valor inválido. Insira a quantidade de eleitores: "))

votes = [0] * 4
nulo = branco = 0

for i in range (maxVoters) :
    voter = int(input("Insira o seu voto: "))
    while voter < 1 or voter > 6 :
        voter = int(input("Voto inválido. Tente novamente: "))
    
    if voter == 5: 
        nulo += 1
    elif voter == 6 :
        branco += 1
    else :
        votes[voter - 1] += 1

winner = 0
maxVotes = 0
for i in range (4) :
    if votes[i] > maxVotes :
        winner = i 
        maxVotes = votes[i]
maxVotes += branco
print("O ganhador foi %s com %i votos" %(candidatos[winner], maxVotes))
print("O resultado geral foi: ")
for i in range (4) :
    print(str(candidatos[i]) + " - " + str(votes[i]))
print("Houveram %i votos nulos e %i votos em branco." %(nulo, branco))
print("A porcentagem de votos nulos em relação ao total é de %i" %((nulo / maxVoters) * 100) + "%")
print("A porcentagem de votos em branco em relação ao total é de %i" %((branco / maxVoters) * 100) + "%")