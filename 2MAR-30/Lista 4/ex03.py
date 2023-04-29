""" Implemente um programa que exiba a tabuada de um número x.
Obs: tabuada: x*1, x*2 … x*10; """

n = int(input("Insira o número que será mostrado a tabuáda: "))

for i in range (1 , 11) :
    print("%i x %i = %i" %(n, i, n*i))