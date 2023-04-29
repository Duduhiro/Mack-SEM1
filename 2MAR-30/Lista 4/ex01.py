""" Implemente um programa que encontre o quinto número maior que 1000, cuja divisão por 11 tenha
resto 5. """
counter = 1
n = 1000

while counter < 5 :
    if n % 11 == 5 :
        counter += 1
        n += 1
    else :
        n += 1
print("O número é %i" %(n))
