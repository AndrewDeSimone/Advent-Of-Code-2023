data = 'real' #test/real
input = open(f'Day 8\star1\\{data}input.txt', 'r').read().split('\n')

sequence = input[0]
input = input[2:]

networkMap = {}

for i in input:
    i = i.split(' = ')
    key = i[0]
    value = [i[1][1:4], i[1][6:9]]
    networkMap[key] = value

node = 'AAA'
count = 0
while True:
    for i in sequence:
        if i == 'L':
            node = networkMap[node][0]
        else:
            node = networkMap[node][1]
        count += 1
        if node == 'ZZZ':
            print(count)
            quit()