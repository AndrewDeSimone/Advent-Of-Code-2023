import re
import functools

data = 'real' #test/real
input = open(f'Day 7\star2\\{data}input.txt', 'r').read().split('\n')
input = [x.split(' ') for x in input]

cardLabels = {'A': 'B', 'K': 'C', 'Q': 'D', 'J': 'Z', 'T': 'F', '9': 'G', '8': 'H', '7': 'I', '6': 'J', '5': 'K', '4': 'L', '3': 'M', '2': 'N', '1': 'O'}
cardBids = {}
cards = []

for i in range(0, len(input)):
    card = input[i][0]
    temp = ''
    for j in card:
        temp += cardLabels[j]
    temp = "".join(temp)
    cardBids[temp] = input[i][1]
    cards.append(temp)

def removeJoker(card):
    if 'Z' in card:
        counts = {}
        for i in card:
            if i != 'Z':
                if i in counts.keys():
                    counts[i] += 1
                else:
                    counts[i] = 1
        mostCommon = next(iter(counts))
        for i in counts.keys():
            if counts[mostCommon] < counts[i]:
                mostCommon = i
        temp = ''
        for i in card:
            if i == 'Z':
                temp += mostCommon
            else:
                temp += i
    else:
        return card
    return temp

#return 1 when card 1 wins
def compareCards(card1, card2):
    
    if card1 == 'ZZZZZ':
        if card2 != 'ZZZZZ':
            if(re.search(r'(.)\1{4}', removeJoker(card2))):
                return -1
            else:
                return 1
        return 0
    
    if card2 == 'ZZZZZ':
        if card1 != 'ZZZZZ':
            if(re.search(r'(.)\1{4}', removeJoker(card1))):
                return 1
            else:
                return -1
        return 0

    card1noj = removeJoker(card1)
    card2noj = removeJoker(card2)

    #5 of a kind
    if(re.search(r'(.)\1{4}', card1noj)):
        if(re.search(r'(.)\1{4}', card2noj)):
            for i in range(0,5):
                if ord(card1[i]) < ord(card2[i]):
                    return 1
                elif ord(card1[i]) > ord(card2[i]):
                    return -1
            return 0
        else:
            return 1
    
    if(re.search(r'(.)\1{4}', card2noj)):
        return -1
    #four of a kind
    if(re.search(r'.?(.).?\1.?\1.?\1.?', card1noj)):
        if(re.search(r'.?(.).?\1.?\1.?\1.?', card2noj)):
            for i in range(0,5):
                if ord(card1[i]) < ord(card2[i]):
                    return 1
                elif ord(card1[i]) > ord(card2[i]):
                    return -1
            return 0
        else:
            return 1
    if(re.search(r'.?(.).?\1.?\1.?\1.?', card2noj)):
        return -1
    #count number of unique
    sCard1 = ''.join(sorted(card1noj))
    sCard2 = ''.join(sorted(card2noj))
    uCard1 = ''
    uCard2 = ''
    for i in card1:
        if not i in uCard1 and i != 'Z':
            uCard1 += i
    for i in card2:
        if not i in uCard2 and i != 'Z':
            uCard2 += i
    uCard1 = len(uCard1)
    uCard2 = len(uCard2)

    #full house
    if(uCard1 == 2):
        if(uCard2==2):
            for i in range(0,5):
                if ord(card1[i]) < ord(card2[i]):
                    return 1
                elif ord(card1[i]) > ord(card2[i]):
                    return -1
            return 0
        else:
            return 1
    if(uCard2==2):
        return -1
    
    #three of a kind
    if(re.search(r'(.)\1\1..', sCard1) or re.search(r'..(.)\1\1', sCard1) or re.search(r'.(.)\1\1.', sCard1)):
        if(re.search(r'(.)\1\1..', sCard2) or re.search(r'..(.)\1\1', sCard2) or re.search(r'.(.)\1\1.', sCard2)):
            for i in range(0,5):
                if ord(card1[i]) < ord(card2[i]):
                    return 1
                elif ord(card1[i]) > ord(card2[i]):
                    return -1
            return 0
        else:
            return 1
    if(re.search(r'(.)\1\1..', sCard2) or re.search(r'..(.)\1\1', sCard2) or re.search(r'.(.)\1\1.', sCard2)):
        return -1
    
    #two pair
    if(re.search(r'.?(.)\1.?(.)\2.?', sCard1)):
        if(re.search(r'.?(.)\1.?(.)\2.?', sCard2)):
            for i in range(0,5):
                if ord(card1[i]) < ord(card2[i]):
                    return 1
                elif ord(card1[i]) > ord(card2[i]):
                    return -1
            return 0
        else:
            return 1
    if(re.search(r'.?(.)\1.?(.)\2.?', sCard2)):
        return -1

    #One Pair
    if(uCard1==4):
        if(uCard2==4):
            for i in range(0,5):
                if ord(card1[i]) < ord(card2[i]):
                    return 1
                elif ord(card1[i]) > ord(card2[i]):
                    return -1
            return 0
        else:
            return 1
    if(uCard2==4):
        return -1
    
    #high card
    for i in range(0,5):
        if ord(card1[i]) < ord(card2[i]):
            return 1
        elif ord(card1[i]) > ord(card2[i]):
            return -1
    return 0

cards = sorted(cards, key = functools.cmp_to_key(compareCards))
sum = 0

for i in range(0, len(cards)):
    sum += int(cardBids[cards[i]]) * (i+1)

print(sum)
#print(cards)