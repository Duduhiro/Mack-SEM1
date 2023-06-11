salas, tuneis = [int(i) for i in input().split()]

tunel_sala = []
for i in range (tuneis) :
    tunel_sala.append([int(j) for j in input().split()])
passeios = int(input())
trajetos = []
possiveis = 0
for i in range (passeios) :
    trajetos.append([int(j) for j in input().split()])
    contador = 0
    for k in range (1, len(trajetos[i]) - 1) :
        for l in range (len(tunel_sala)) :
            if trajetos[i][k] in tunel_sala[l] and trajetos[i][k + 1] in tunel_sala[l] :
                contador += 1
    if contador == (trajetos[i][0] - 1) :
        possiveis += 1
print(possiveis)
