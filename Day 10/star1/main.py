data = 'real' #test/real
input = open(f'Day 10\star1\\{data}input.txt', 'r').read().split('\n')

for i in range(0, len(input)):
    input[i] = list(input[i])

startingPoint = (0,0)
testHard = 'F'
realHard = 'J'

#find starting point
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            startingPoint = (i, j)
            if data == 'test':
                input[i][j] = testHard
            else:
                input[i][j] = realHard


toVisit = [[startingPoint]]

i = 0

while len(toVisit[i]) != 0:
    toVisit.append([])
    for j in toVisit[i]:
        check = []
        current = input[j[0]][j[1]]
        input[j[0]][j[1]] = '.'
        if current == '|':
            check = [(j[0]-1, j[1]),(j[0]+1, j[1])]
        if current == '-':
            check = [(j[0], j[1]-1),(j[0], j[1]+1)]
        if current == 'L':
            check = [(j[0]-1, j[1]),(j[0], j[1]+1)]
        if current == 'J':
            check = [(j[0]-1, j[1]),(j[0], j[1]-1)]
        if current == '7':
            check = [(j[0]+1, j[1]),(j[0], j[1]-1)]
        if current == 'F':
            check = [(j[0]+1, j[1]),(j[0], j[1]+1)]
        for q in check:
            if input[q[0]][q[1]] != '.':
                toVisit[i+1].append(q)
    i += 1

print(len(toVisit)-2)