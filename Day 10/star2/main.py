data = 'real' #test/real
input = open(f'{data}input.txt', 'r').read().split('\n')

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

visited = []
toVisit = [[startingPoint]]

i = 0

while len(toVisit[i]) != 0:
    toVisit.append([])
    for j in toVisit[i]:
        visited.append(j)
        check = []
        current = input[j[0]][j[1]]
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
            if q not in visited:
                toVisit[i+1].append(q)
    i += 1


for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        if (i, j) not in visited:
            input[i][j] = '.'

asciiMap = {'.': '.', '|': '│', '-': '─', 'F': '┌', 'J': '┘', '7': '┐', 'L': '└'}
#block gaps
for i in range(0,len(input)):
    for j in range(0,len(input[0])):
        input[i][j] = asciiMap[input[i][j]]

print()
print()
print()
print()

for i in input:
    for j in i:
        print(j, end='')
    print()

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()