""" Implemente um programa que exiba a tabuada de um número x.
Obs: tabuada: x*1, x*2 … x*10; """

x = int(input("X: "))
for i in range (1, 11) :
    print(f"{x} x {i} = {x * i}")