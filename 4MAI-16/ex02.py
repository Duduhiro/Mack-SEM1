lista = []
for i in range (10) :
    lista.append(int(input()))
procurar = int(input())
if procurar in lista :
    print("NÚMERO EXISTE")
else :
    print("NÚMERO NÃO EXISTE")
    