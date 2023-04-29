# Esse programa printa uma pirâmide do estilo mário do tamanho que o usuário pedir

size = int(input("Insira o tamanho da pirâmide (entre 3 - 8): "))

while size < 3 or size > 8 :
    print("Valor incorreto!")
    size = int(input("Insira o tamanho novamente: "))

loop = 1
reversed = size
for i in range (size) :
    for k in range (reversed) :
        print(" ", end="")
    for j in range (loop) :
        print("#", end="")
    for j in range (loop) :
        print("#", end="")
    reversed -= 1
    loop += 1
    print("")
