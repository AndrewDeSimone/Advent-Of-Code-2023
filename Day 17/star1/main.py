from heapq import heappush, heappop

data = 'real' #test/real
input = open(f'Day 17\star1\\{data}input.txt', 'r').read().split('\n')
input = [list(map(int, line.strip())) for line in input]

seen = set()
heap = [(0, 0, 0, 0, 0, 0)]

while heap:
    heatLoss, row, column, directionRow, directionColumn, n = heappop(heap)

    if row == len(input) - 1 and column == len(input[0])-1:
        print(heatLoss)
        break

    if (row, column, directionRow, directionColumn, n) in seen:
        continue

    seen.add((row, column,directionRow, directionColumn, n))

    if n < 3 and (directionRow, directionColumn) != (0,0):
        nextRow = directionRow + row
        nextColumn = directionColumn + column
        if 0 <= nextRow < len(input) and 0 <= nextColumn < len(input[0]):
            heappush(heap, (heatLoss + input[nextRow][nextColumn], nextRow, nextColumn, directionRow, directionColumn, n+1))
    
    for nextDirectionRow, nextDirectionColumn in [(0,1), (1,0), (0,-1), (-1, 0)]:
        if (nextDirectionRow, nextDirectionColumn) != (directionRow, directionColumn) and (nextDirectionRow, nextDirectionColumn) != (-directionRow, -directionColumn):
            nextRow = nextDirectionRow + row
            nextColumn = nextDirectionColumn + column
            if 0 <= nextRow < len(input) and 0 <= nextColumn < len(input[0]):
                heappush(heap, (heatLoss + input[nextRow][nextColumn], nextRow, nextColumn, nextDirectionRow, nextDirectionColumn, 1))
