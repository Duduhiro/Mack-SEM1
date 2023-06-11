saldo = int(input())
contas = []
for i in range (3) :
    contas.append(int(input()))
contas.sort()
pagar = 0
for i in range (3) :
    if saldo >= contas[i] :
        pagar += 1
        if i != 2 :
            contas [i + 1] += contas[i]
    else :
        break
print(pagar)