"""  Implemente um programa que exiba a tabuada de um número x.
Obs: tabuada: x*1, x*2 … x*10; """
x = int(input("N: "))
print(f'Tabuada do {x}: ')
for i in range (1, 11) :
    print(f'{i:2.0f} * {x} = {i * x}')