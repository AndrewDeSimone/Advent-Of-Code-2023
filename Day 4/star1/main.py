import re

data = 'real' #test/real
input = open(f'Day 4\star1\\{data}input.txt', 'r').read().split('\n')

sum = 0

for i in input:
    temp = numbers = i.split(':')[1]
    winners = re.findall('\d+', temp.split('|')[0])
    numbers = re.findall('\d+', temp.split('|')[1])
    count = 0
    for i in numbers:
        if i in winners:
            if count == 0:
                count = 1
            else:
                count *= 2
    sum += count

print(sum)