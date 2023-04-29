"""BlackJack, ou 21, é um jogo na qual o objetivo é somar cartas o mais próximo de 21,
sem ultrapassar """
import random

def randCard():
    card = random.randint(1, 10)
    return card

print("----- BLACK JACK -----")
chips = 1000
print("CHIPS: %i" %(chips))
bet = 0

while chips != 0 :
    busted = 1
    turn = 1
    card1 = 0
    card2 = 0
    bet = int(input("Insert bet (-1 to end): "))
    if bet == -1 :
        break
    card1 = randCard()
    card2 = randCard()
    total = card1 + card2
    dealer1 = randCard()
    dealer2 = randCard()
    dealerTotal = dealer1 + dealer2 
    print("Your cards: %i | %i" %(card1, card2))
    print("Your total is %i" %(total))
    print("Dealer drew a %i" %(dealer1))

    while busted == 1 :
        if turn == 1 :
            play = input("Hit or stay: ")
            play = play.lower
            while play != "hit" and play != "stay" :
                play = input("ERROR! Hit or stay: ")
            if play == "hit" and total < 21:
                card1 = randCard()
                total += card1
                print("You drew a %i" %(card1))
                print("Your total is %i" %(total))
            else :
                busted = 2
            turn += 1
        else : 
            if dealerTotal < 17 :
                print("Dealer choose hit")
                dealer1 = randCard() 
                dealerTotal += dealer1
                print("Dealer drew a %i" %(dealer1))    
                print("Dealer total is %i" %(dealerTotal))
        turn -= 1
    if total <= 21 and total > dealerTotal :
        chips += bet
        print("Win")
    elif total > 21 or (dealerTotal <= 21 and dealerTotal > total):
        chips -= bet
        print("Lost")
    print("CHIPS: %i" %(chips))    


    