#Given a list, hand containing five strings (the cards), implement a function called poker_hand_ranking that returns a 
#string with the name of the highest combination obtained.
import random
from collections import Counter
def poker_hand_ranking(hand):
    #break apart hand into num and suit
    # sort the hand in ascending order (numbers and letters will vary sorting type)
    suits, numbers = suit_and_number_splitter(hand)
    numberdict = {}
    for nums in numbers:
        if nums not in numberdict:
            numberdict[nums] =1
        else:
            numberdict[nums]+=1
    
    #Check for flush and straight (royal or straight flush)
    if is_a_flush(suits) and is_a_straight(numbers):
        if numbers == [1,10,11,12,13]:
            # print('Royal Flush')
            return(10)
        else:
            # print('Straight Flush')
            return(9)
    #check for flush without a straight
    elif is_a_flush(suits) and not is_a_straight(numbers):
        # print('Flush')
        return(8)
    #check for straight without a flush
    elif not is_a_flush(suits) and is_a_straight(numbers):
        # print('Straight')
        return(7)

    else:
        if is_a_four_of_a_kind(numberdict):
            # print('4 of a kind')
            return(6)
        elif is_a_three_of_a_kind(numberdict) and is_a_pair(numberdict):
            # print('Full House')
            return(5)
        elif is_a_three_of_a_kind(numberdict) and not is_a_pair(numberdict):
            # print('3 of a kind')
            return(4)
        elif is_a_two_pair(numberdict):
            # print('2 Pair')
            return(3)
        elif is_a_pair(numberdict) and not is_a_three_of_a_kind(numberdict):
            # print('Pair')
            return(2)
        else:
            # print("High Card")
            return(1)
        #Check how many
    # do a check if there are > 2 num with a counter
    # if there are 2, pair, 3 , three of a kind , 4 , 4 of a kind
    # assign the cards a winning rank (useful for determining winner later)

def suit_and_number_splitter(hand):
    cardnumbers = []
    cardsuits = [] 
    facenumber = 11
    for i in hand:
        eachcard = i.split()
    #suits
        cardsuits.append(eachcard[0][len(eachcard[0])-1])
        
    #numbers
        if len(eachcard[0]) == 3:
            cardnumbers.append(int(eachcard[0][0:2])) 
        else: #not 10
            if(eachcard[0][0:1] == 'J'):
                facenumber = 11
            elif (eachcard[0][0:1] == 'Q'):
                facenumber = 12
            elif (eachcard[0][0:1] == 'K'):
                facenumber = 13
            elif (eachcard[0][0:1] == 'A'):
                facenumber = 1
            else:
                facenumber = int(eachcard[0][0:1])
            cardnumbers.append(facenumber)
    return cardsuits, sorted(cardnumbers)
def is_a_flush(suits):
    suitdict = {}
    for letter in suits:
        if letter not in suitdict:
            suitdict[letter] = 1
        else:
            suitdict[letter]+=1
    return len(suitdict) == 1
def is_a_four_of_a_kind(i):
    return 4 in i.values()
def is_a_three_of_a_kind(i):
    return 3 in i.values()
def is_a_pair(i):
    return 2 in i.values() 
def is_a_two_pair(i):
    return [2,2] == [
        Counter(i).most_common(2)[0][1], 
        Counter(i).most_common(2)[1][1]]
def is_a_straight(number):
    return (
        number[len(number)-1]-number[len(number)-2] == 1 and
        number[len(number)-2]-number[len(number)-3] == 1 and
        number[len(number)-3]-number[len(number)-4] == 1 and
        number[len(number)-4]-number[len(number)-5] == 1
        ) or (
        number[len(number)-1]-number[len(number)-2] == 1 and
        number[len(number)-2]-number[len(number)-3] == 1 and
        number[len(number)-3]-number[len(number)-4] == 1 and
        number[len(number)-4]-number[len(number)-5] == 9
    )

deck_in_hand = []

royalflushhand = ["10h", "Jh", "Qh", "Ah", "Kh"]
straightflushhand = ['Ah','2h','3h','4h','5h']
fourofakindhand = ["10s", "10c", "8d", "10d", "10h"]
fullhousehand = ["2c", "2d", "4d", "4s","4h"]
flushhand = ["6d", "7d", "2d", "Kd", "Jd"]
straighthand = [ "As", "2d", "4h","3d", "5c"]
threeofakindhand = ["10s", "10c", "8d", "10d", "Ah"]
twopairhand = [ "2s", "2d", "3h","3d", "5c"]
pairhand = [ "As", "5d", "4h","3d", "5c"]
highcardhand = ["3h", "5h", "Qs", "9h", "Ad"]

# poker_hand_ranking(royalflushhand)
# poker_hand_ranking(straightflushhand)
# poker_hand_ranking(flushhand)
# poker_hand_ranking(straighthand)
# poker_hand_ranking(fourofakindhand)
# poker_hand_ranking(fullhousehand)
# poker_hand_ranking(threeofakindhand)
# poker_hand_ranking(twopairhand)
# poker_hand_ranking(pairhand)
# poker_hand_ranking(highcardhand)

round_1 = {"John": ["10h", "Jh", "Qh", "Ah", "Kh"], 
"Peter": ["3h", "5h", "Qs", "9h", "Ad"]} 
def winner_is(round_1):
    winning_hand = {}
    for i in round_1:
        winning_hand[i] = poker_hand_ranking(round_1[i])

    return(max(winning_hand, key=winning_hand.get))


print(winner_is(round_1))



#This function will deal out random cards 
# def deal_cards(card,suit):
    # card = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    # suit = ["s","h","d","c"]
#     for i in range(0,5):
        # print(i)
        # print(random.choice(card))
        # if([random.choice(card) + random.choice(suit)]) not in deck_in_hand:
        #     deck_in_hand.append(random.choice(card)[i]+random.choice(suit))

# deal_cards(card,suit)
# print(card,suit,deck_in_hand)