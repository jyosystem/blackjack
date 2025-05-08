import random

deck = [1,2,3,4,5,6,7,8,9,11,12,13]*4*4*100
money = 1000
bet = 10




def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
        return hand
        
def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 1:
        card = "A"
    hand.append(card)
    return hand
def total(hand):
    score = 0
    a=0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score = score + 10
        elif card == "A":
            if score >= 11:
                score = score + 1
            else:
                score += 11
                a+=1
        else:
            score += card
        if(score >= 22 and a>=1):
            score -=10
            a-=1
            
    return score 
def has_duplicates(seq):
    return len(seq) != len(set(seq))   
def result(dealer_hand, player_hand):
    global money
    global bet
    if total(player_hand) > total(dealer_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[32mYOU WIN!\033[0m")
        money += bet*2
    elif total(dealer_hand) > total(player_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[91mYOU LOSE...\033[0m")
    elif total(dealer_hand) == total(player_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[91mDRAW\033[0m")
        money += bet



def game():
    card_number = 0
    dealer_hand = deal()
    player_hand = deal()
    player_handA = player_hand
    dealer_handA = dealer_hand
    hit(player_hand)
    print(f"dealer {dealer_hand[0]} ")
    print(f"player {player_hand} sum {total(player_hand)} ")

    if(player_hand[0] == player_hand[1] and card_number <= 2):
        if(player_hand[0]==2):
            player_hand.pop(0)
            hit(player_hand)
            gamerule(player_hand, dealer_hand)
            player_hand = player_handA
            dealer_hand = dealer_handA
            gamerule(player_hand, dealer_hand)
            card_number+=1
    else:
        gamerule(player_hand, dealer_hand)

    #if(has_duplicates(player_hand)):

    #if(soft == 0):
# def split(player_hand):
#     c=1

def gamerule(player_hand, dealer_hand):
    global money
    global bet
    if ('A' in player_hand):
        soft = 1
    else:
        soft = 0
    print(dealer_hand)
    money-=bet
    choice = "hit"
    while choice != quit:
        if(soft==0):
            if (total(player_hand) == 2):
                if(total(dealer_hand)==6):
                    choice= "double"
            elif(total(player_hand) == 8):
                if(total(dealer_hand)>=5 and total(dealer_hand) <= 7):
                    choice= "double"
            elif(total(player_hand) == 9):
                if(total(dealer_hand)>=2 and total(dealer_hand)<=8):
                    choice= "double"
            elif(total(player_hand) == 10):
                if(total(dealer_hand)>=2 and total(dealer_hand)<=9):
                    choice= "double"
            elif(total(player_hand) == 11):
                if(total(dealer_hand)>=2 and total(dealer_hand)<=10):
                    choice= "double"
            elif(total(player_hand) == 14):
                if(total(dealer_hand)>=4 and total(dealer_hand)<=6):
                    choice= "stand"
            elif(total(player_hand) == 15):
                if(total(dealer_hand)>=2 and total(dealer_hand) <= 6):
                    choice= "stand"
            elif(total(player_hand) == 16):
                if(total(dealer_hand) >= 2 and total(dealer_hand) <= 6):
                    choice= "stand"
                if(total(dealer_hand) == 10 and total(dealer_hand) == 11):
                    choice = "suspend"
            elif(total(player_hand) >= 17):
                choice= "stand"
        elif(soft==1):
            if (total(player_hand) == 13):
                if(total(dealer_hand)>=2 and total(dealer_hand)<=9):
                    choice= "double"
            elif (total(player_hand) == 14):
                if(total(dealer_hand)>=2 and total(dealer_hand)<=9):
                    choice= "double"
            elif (total(player_hand) == 15):
                if(total(dealer_hand)>=2 and total(dealer_hand)<=8):
                    choice= "double"
            elif (total(player_hand) == 16):
                if(total(dealer_hand)>=3 and total(dealer_hand)<=8):
                    choice= "double"
            elif (total(player_hand) == 17):
                if(total(dealer_hand)>=3 and total(dealer_hand)<=7):
                    choice= "double"
            elif (total(player_hand) == 18):
                if(total(dealer_hand)==2):
                    choice= "double"
                elif(total(dealer_hand)>=3 and total(dealer_hand)<=8):
                    choice= "stand"
            elif (total(player_hand) == 19 and total(player_hand) == 20):
                    choice= "stand"
            elif (total(player_hand) == 21):
                    choice= "blackjack"
        if choice == "double":
            money -= bet
            bet = bet*2
            hit(player_hand)
            print(
                f"\nあなたに {player_hand[-1]} が配られ、カードは {player_hand} 合計は {total(player_hand)} です。")
            if total(player_hand) > 21:
                print("あなたは 21 を超えてしまいました。\033[91mYOU LOSE...\033[0m")
                choice = quit
            elif total(player_hand) == 21:
                print("\033[32mYOU WIN!\033[0m")
                money+=bet*2
                choice = quit
        elif choice == "suspend":
            print("suspend------")
            money+=0.5*bet
            choice = quit
        
        elif choice == "blackjack":
            print("\033[32mYOU WIN!\033[0m")
            money += bet*2.5
            choice = quit


        elif choice == "hit":
            hit(player_hand)
            print(
                f"\nあなたに {player_hand[-1]} が配られ、カードは {player_hand} 合計は {total(player_hand)} です。")
            if total(player_hand) > 21:
                print("あなたは 21 を超えてしまいました。\033[91mYOU LOSE...\033[0m")
                choice = quit
            elif total(player_hand) == 21:
                money+=2*bet
                choice = quit
                print("\033[32mYOU WIN!\033[0m")#ソフトハンド考慮

        elif choice == "stand":
            print(
                f"\nディーラーの2枚めのカードは {dealer_hand[-1]} 合計は {total(dealer_hand)} です。")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(
                    f"ディーラーに {dealer_hand[-1]} が配られ、カードは {dealer_hand} 合計は {total(dealer_hand)} です。")
                if total(player_hand) == 21:
                    print("\033[91m you WIN\033[0m")
                    money+=bet*2
                    choice = quit
                elif total(dealer_hand) > 21:
                    print("ディーラーは 21 を超えてしまいました。\033[32mYOU WIN!\033[0m")
                    
                    money += bet*2
                    
                    choice = quit
        

            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                choice = quit
        if(choice == quit):

            print(f"current money = {money}")
            bet = 10
        
def game2():
    num=0
    while num<10:
        game()
        num+=1

game2()

