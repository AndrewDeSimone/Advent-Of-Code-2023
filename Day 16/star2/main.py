import sys
data = 'real' #test/real
input = open(f'Day 16\star2\\{data}input.txt', 'r').read().split('\n')
sys.setrecursionlimit(10000)

def rayTrace(coordinate, direction, grid, history):
    #CHECK FOR OUT OF BOUNDS
    if coordinate[0] < 0 or coordinate[0]==len(grid) or coordinate[1]<0 or coordinate[1]==len(grid[0]):
        return
    #handle double visits
    if coordinate in history.keys():
        if direction in history[coordinate]:
            return
        history[coordinate].append(direction)
    else:
        history[coordinate] = [direction]
    
    #handle instructions
    instruction = grid[coordinate[0]][coordinate[1]]
    if instruction == '.' or (direction in ['right', 'left'] and instruction == '-') or (direction in ['up', 'down'] and instruction == '|'):
        if direction == 'right':
            rayTrace((coordinate[0], coordinate[1]+1), direction, grid, history)
        elif direction == 'left':
            rayTrace((coordinate[0], coordinate[1]-1), direction, grid, history)
        elif direction == 'up':
            rayTrace((coordinate[0]-1, coordinate[1]), direction, grid, history)
        elif direction == 'down':
            rayTrace((coordinate[0]+1, coordinate[1]), direction, grid, history)
    elif instruction == '|':
        rayTrace((coordinate[0]-1, coordinate[1]), 'up', grid, history)
        rayTrace((coordinate[0]+1, coordinate[1]), 'down', grid, history)
    elif instruction == '-':
        rayTrace((coordinate[0], coordinate[1]+1), 'right', grid, history)
        rayTrace((coordinate[0], coordinate[1]-1), 'left', grid, history)
    elif instruction == '\\':
        if direction == 'right':
            rayTrace((coordinate[0]+1, coordinate[1]), 'down', grid, history)
        elif direction == 'left':
            rayTrace((coordinate[0]-1, coordinate[1]), 'up', grid, history)
        elif direction == 'up':
            rayTrace((coordinate[0], coordinate[1]-1), 'left', grid, history)
        elif direction == 'down':
            rayTrace((coordinate[0], coordinate[1]+1), 'right', grid, history)
    elif instruction == '/':
        if direction == 'right':
            rayTrace((coordinate[0]-1, coordinate[1]), 'up', grid, history)
        elif direction == 'left':
            rayTrace((coordinate[0]+1, coordinate[1]), 'down', grid, history)
        elif direction == 'up':
            rayTrace((coordinate[0], coordinate[1]+1), 'right', grid, history)
        elif direction == 'down':
            rayTrace((coordinate[0], coordinate[1]-1), 'left', grid, history)

def localizedRayTrace(coordinate, direction, grid):
    history = {}
    rayTrace(coordinate, direction, grid, history)
    return len(history)

most = 0


for i in range(0,len(input)):
    most = max(most, localizedRayTrace((i,0), 'right', input))
    most = max(most, localizedRayTrace((i,len(input[0])-1), 'left', input))
for i in range(0,len(input[0])):
    most = max(most, localizedRayTrace((0,i), 'down', input))
    most = max(most, localizedRayTrace((len(input)-1,i), 'up', input))

print(most)

