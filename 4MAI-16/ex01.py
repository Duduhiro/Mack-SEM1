lista = []
for i in range(10) :
    lista.append(input())

vogal = 0
consoante = 0 

for i in lista :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': 
        vogal += 1
    else :
        consoante += 1
print(vogal)
print(consoante)