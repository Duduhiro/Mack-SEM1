""" Implemente um programa que encontre o quinto número maior que 1000, cuja divisão por 11 tenha
resto 5. """
n = 1000
counter = 0 
while True :
    if n % 11 == 5 :
        counter += 1
    if counter == 5 :
        break
    n += 1
print(n)