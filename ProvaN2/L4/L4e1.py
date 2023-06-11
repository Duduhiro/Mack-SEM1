""" 1) Implemente um programa que encontre o quinto número maior que 1000, cuja divisão por 11 tenha 
resto 5. """
n = 1000
for i in range (5) :
    n += 1
    while n % 11 != 5 :
        n += 1
print(f'Quinto número maior que 1000 cuja divisão por 1 tenha resto 5: {n}')
