tipo, tamanho = [int(i) for i in input().split()]
estoque = []
for i in range (tipo) :
    estoque.append([int(j) for j in input().split()])
p = int(input())
compras = []
possiveis = 0
for i in range (p) :
    compras.append([int(j) for j in input().split()])
    if estoque[compras[i][0] - 1][compras[i][1] - 1] > 0 :
        estoque[compras[i][0] - 1][compras[i][1] - 1] -= 1
        possiveis += 1
print(possiveis)

