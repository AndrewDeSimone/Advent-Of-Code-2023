import math

data = 'real' #test/real
input = open(f'Day 8\star2\\{data}input.txt', 'r').read().split('\n')

sequence = input[0]
input = input[2:]

networkMap = {}
nodes = []

for i in input:
    i = i.split(' = ')
    key = i[0]
    if key[2] == 'A':
        nodes.append(key)
    value = [i[1][1:4], i[1][6:9]]
    networkMap[key] = value


for q in range(len(nodes)):
    count = 0
    temp = nodes[q]
    found = False
    while not found:
        for i in sequence:
            if i == 'L':
                temp = networkMap[temp][0]
            else:
                temp = networkMap[temp][1]
            count += 1
            found = False
            if temp[2] == 'Z':
                nodes[q] = count
                found = True

print(math.lcm(*nodes))