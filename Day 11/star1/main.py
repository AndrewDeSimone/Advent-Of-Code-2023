data = 'real' #test/real
input = open(f'Day 11\star1\\{data}input.txt', 'r').read().split('\n')

#make strings lists
for i in range(0, len(input)):
    input[i] = list(input[i])

galaxies = 0
galaxyMap = {}
#add numbers
for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        if input[i][j] == '#':
            galaxies += 1
            input[i][j] = galaxies
            galaxyMap[galaxies] = (i,j)

emptyRows = []
for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        if input[i][j] != '.':
            break
        if j == len(input[0]) -1:
            emptyRows.append(i)

emptyColumns = []
for i in range(0,len(input[0])):
    for j in range(0, len(input)):
        if input[j][i] != '.':
            break
        if j == len(input[0]) -1:
            emptyColumns.append(i)

sum = 0
for i in range(1, galaxies):
    for j in range(i, galaxies+1):
        distance = 0
        manX = abs(galaxyMap[i][0] - galaxyMap[j][0])
        manY = abs(galaxyMap[i][1] - galaxyMap[j][1])
        distance += manX + manY
        passedRows = list(range(galaxyMap[i][0], galaxyMap[j][0])) + list(range(galaxyMap[j][0], galaxyMap[i][0]))
        for k in passedRows:
            if k in emptyRows:
                distance += 1
        passedColumns = list(range(galaxyMap[i][1], galaxyMap[j][1])) + list(range(galaxyMap[j][1], galaxyMap[i][1]))
        for k in passedColumns:
            if k in emptyColumns:
                distance += 1
        sum += distance
                



print(sum)