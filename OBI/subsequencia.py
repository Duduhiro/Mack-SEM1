list_a_size, list_b_size = [int(i) for i in input().split()]
list_a = [int(i) for i in input().split()]
list_b = [int(i) for i in input().split()]

for i in range (list_a_size  - (list_b_size - 1)) :
    if list_a[i] == list_b[0] :
        for j in range (1, list_b_size) :
            for k in range (i + 1, list_a_size) :
                if list_a[k] == list_b[j] :
                    i += 1
                    break
                else :
                    i += 1
            else :
                break
        else :
            print('S')
            break
else :
    print('N')
