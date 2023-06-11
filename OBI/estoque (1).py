tipo, size = [int(i) for i in input().split()]

estoque = []
for i in range (tipo) :
    estoque.append([int(j) for j in input().split()])

pedidos = int(input())
local_pedidos = []
compras = 0
for i in range (pedidos) :
    local_pedidos.append([int(j) for j in input().split()])
    if estoque[(local_pedidos[i][0] - 1)][(local_pedidos[i][1] - 1)] > 0 :
        compras += 1
        estoque[(local_pedidos[i][0] - 1)][(local_pedidos[i][1] - 1)] -= 1
print(compras)