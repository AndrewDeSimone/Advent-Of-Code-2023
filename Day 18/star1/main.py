data = 'real' #test/real
input = open(f'Day 18\star1\\{data}input.txt', 'r').read().split('\n')

polygon = [(0,0)]

for i in input:
    direction, distance, color = i.split(' ')
    distance = int(distance)
    x, y = polygon[len(polygon)-1]
    if direction == 'R':
        polygon.append((x+distance, y))
    if direction == 'L':
        polygon.append((x-distance, y))
    if direction == 'U':
        polygon.append((x, y+distance))
    if direction == 'D':
        polygon.append((x, y-distance))

def getAreaUsingShoelace(polygon):
    total = 0
    for i in range(0, len(polygon)-1):
        total += polygon[i][0] * polygon[i+1][1]
    for i in range(1,len(polygon)):
        total -= polygon[i][0] * polygon[i-1][1]

    #add perimteter?
    perimeter = 0
    for i in range(len(polygon)-1):
        perimeter += abs(polygon[i][0]-polygon[i+1][0]) + abs(polygon[i][1]-polygon[i+1][1])
    total = perimeter + abs(total)
    return int(total/2) + 1

print(getAreaUsingShoelace(polygon))