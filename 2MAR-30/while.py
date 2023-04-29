x = int(input("Número: "))

loop = 0
i = 1 

while loop == 0 :
    if i * i < x :
        if (i + 1) * (i + 1) > x :
            break
        else :
            i += 1
    else :
        i += 1
print(i)