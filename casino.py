import random
money = 10
valid = True
while money>0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    print("Money: " + str(money))
    bet = int(input("Bet Amount: "))
    if bet == 0:
        money =0
        break
    elif bet>4:
        valid = False
    while valid == False:
        print("invalid Bet")
        bet = int(input("Bet Amount: "))
        if bet==0:
            valid = True
            money =0
        elif bet <=4:
            valid = True
            

    print("Dice 1: " + str(dice1) + "\nDice 2: " + str(dice2) + "\nDice 3: " + str(dice3))
    
    money -=bet
    if dice1==dice2==dice3:
        bet*=10
        print("You made " + str(bet) + " dollars")
        money+=bet
    elif dice1==dice2 or dice1==dice3 or dice2==3:
        bet*=7
        print("You made " + str(bet) + " dollars")
        money+=bet
    elif (dice1%2==0 and dice2%2==0 and dice3%2==0) or (dice1%2!=0 and dice2%2!=0 and dice3%2!=0):
        bet*=5
        print("You made " + str(bet) + " dollars")
    else:
        print("You lost " + str(bet) + " dollars")
if money<=0:
    print("Go play anoter game")
