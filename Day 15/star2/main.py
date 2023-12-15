data = 'real' #test/real
input = open(f'Day 15\star2\\{data}input.txt', 'r').read().split(',')

def hash(s):
    value = 0
    for i in s:
        value += ord(i)
        value *= 17
        value %= 256
    return value

boxes = [[] for i in range(0,256)]

for i in input:
    if '=' in i:
        found = False
        i = i.split('=')
        code = hash(i[0])
        for j in range(len(boxes[code])):
            if i[0] in boxes[code][j]:
                boxes[code][j] = f'{i[0]} {i[1]}'
                found = True
        if not found:
            boxes[code].append(f'{i[0]} {i[1]}')

    if '-' in i:
        i = i.split('-')
        code = hash(i[0])
        for j in boxes[code]:
            if i[0] in j:
                boxes[code].remove(j)

total = 0

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total += (i+1) * (j+1) * int(boxes[i][j].split(' ')[1])

print(total)