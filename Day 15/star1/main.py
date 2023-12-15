data = 'real' #test/real
input = open(f'Day 15\star1\\{data}input.txt', 'r').read().split(',')

total = 0

def hash(s):
    value = 0
    for i in s:
        value += ord(i)
        value *= 17
        value %= 256
    return value

for i in input:
    total += hash(i)

print(total)
