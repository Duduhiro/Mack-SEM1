size = int(input("Tamanho do quadrado: "))
print('* ' * size)
for i in range (size - 2) :
    print('* ', end='')
    print('  ' * (size - 2), end ="*\n")
print('* ' * size)