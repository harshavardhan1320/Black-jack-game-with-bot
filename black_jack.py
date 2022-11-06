import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p1=random.choice(cards)
p2=random.choice(cards)
player_cards=[p1,p2]

print("your cards :",player_cards)

c1=random.choice(cards)
c2=random.choice(cards)
computer_cards=[c1,c2]

print("computer's first card :",c1)

choice=input("Type 'y' to get an another card , type 'n' to pass :")
if choice == "y":
    draw = True
    while draw:
        rc=random.choice(cards)
        player_cards.append(rc)
        print("your cards :",player_cards)
        if sum(player_cards) > 21:
            draw = False
        else:
            player_draw=input("you woild still like to draw a card y or n :")
            if player_draw == "n":
                draw = False
            

t1=sum(player_cards)
t2=sum(computer_cards)
while t2 < 14 or t2 < t1: 
    rc1=random.choice(cards)
    computer_cards.append(rc1)



print("your final cards :",player_cards)
print("computers final cards :",computer_cards)
t1=sum(player_cards)
t2=sum(computer_cards)
if t1 > 21 or t2 > 21:
    if t1 > t2:
        print(f"you loose the game :(")
    else:
        print(f"you won the game :)")
elif t1==t2:
    print("The game has drawn ")
elif t1 < t2:
    print("you loose :(")
elif t1 > t2:
    print("you have won the game ;)")





