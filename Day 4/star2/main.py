import re

data = 'real' #test/real
input = open(f'Day 4\star1\\{data}input.txt', 'r').read().split('\n')

cards = []

for i in input:
    cards.append(i.split(':')[1])

def evaluate(card):
    current = cards[card]
    if isinstance(current, int):
        return current
    matches = 0
    winners = re.findall('\d+', current.split('|')[0])
    numbers = re.findall('\d+', current.split('|')[1])
    for i in numbers:
        if i in winners:
            matches += 1
    if matches == 0:
        cards[card] = 1
        return 1
    cards[card] = sum([evaluate(i) for i in range(card+1, card+matches+1)])+1
    return cards[card]


print(sum([evaluate(i) for i in range(len(cards))]))