data = 'real' #test/real
input = open(f'Day 21\star1\\{data}input.txt', 'r').read().split('\n')

start = None

for i in range(0,len(input)):
    for j in range(0 , len(input[0])):
        if input[i][j] == 'S':
            start = (i, j)

steps = 64
toVisit = {i:set() for i in range(steps+1)}
toVisit[0].add(start)

for i in range(steps):
    for j in toVisit[i]:
        #up
        if j[0] > 0:
            if input[j[0]-1][j[1]] != '#':
                toVisit[i+1].add((j[0]-1, j[1]))
        #down
        if j[0] < len(input)-1:
            if input[j[0]+1][j[1]] != '#':
                toVisit[i+1].add((j[0]+1, j[1]))
        #left
        if j[1] > 0:
            if input[j[0]][j[1]-1] != '#':
                toVisit[i+1].add((j[0], j[1]-1))
        #right
        if j[1] < len(input[0])-1:
            if input[j[0]][j[1]+1] != '#':
                toVisit[i+1].add((j[0],j[1]+1))




print(len(toVisit[steps]))
