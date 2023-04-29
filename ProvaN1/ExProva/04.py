n1 = 56
n2 = 32

while n1 > 0 and n2 > 0 :
    if n1 > n2 :
        n1 = n1 - n2
    else :
        n2 = n2 - n1

if n1 > 0 :
    print("n1", n1)
else :
    print("n2", n2)