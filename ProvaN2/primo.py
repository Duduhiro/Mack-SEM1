n = int(input("N: "))

for i in range (2, int(n/2 + 1)) :
    if n % i == 0 :
        print('Não primo')
        break
else :
    print('Primo')