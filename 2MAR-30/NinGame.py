name1 = input("Player 1, enter your name: ")
name2 = input("Player 2, enter your name: ")

a = 3
b = 4 
c = 5
seletor = 1

print("A: %i | B: %i | C: %i" %(a, b, c))

while (a + b + c != 0) :
    if seletor == 1 :
        pile = input("%s, choose a pile: " %(name1))
        seletor += 1
    else :
        pile = input("%s, choose a pile: " %(name2))
        seletor -= 1
    
    pile = pile.lower()
    if pile != "a" and pile != "b" and pile != "c" :
        print("Error! Incorrect command")
    else :
        if pile == "a" :
            remove = int(input("How many to remove from pile A: "))
            a -= remove
        elif pile == "b" :
            remove = int(input("How many to remove from pile B: "))
            b -= remove
        else :
            remove = int(input("How many to remove from pile C: "))
            c -= remove
    print("A: %i | B: %i | C: %i" %(a, b, c))

if seletor == 1 : 
    print("%s, YOU WON!" %(name1))
else :
    print("%s, YOU WON!" %(name2))    
    