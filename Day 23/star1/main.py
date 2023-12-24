data = 'real' #test/real
input = open(f'Day 23\star1\\{data}input.txt', 'r').read().split('\n')

start = (0, input[0].index('.'))
end = (len(input)-1, input[-1].index('.'))
points = [start, end]


for r, row in enumerate(input):
    for c, col in enumerate(row):
        if col == '#':
            continue
        neighbors = 0
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < len(input) and 0 <= nc < len(input[0]) and input[nr][nc] != '#':
                neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

graph = {pt: {} for pt in points}

dirs = {
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '>': [(0, 1)],
    '.': [(-1, 0), (1, 0), (0,-1), (0, 1)]
}

for sr, sc in points:
    stack = [(0, sr, sc)]
    seen = {(sr, sc)}

    while stack:
        n, r, c = stack.pop()

        if n != 0 and (r, c) in points:
            graph[(sr, sc)][(r, c)] = n
            continue

        for dr, dc in dirs[input[r][c]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(input) and 0 <= nc < len(input[0]) and input[nr][nc] != '#' and (nr, nc) not in seen:
                stack.append((n+1, nr, nc))
                seen.add((nr, nc))

seen = set()

def dfs(pt):
    if pt == end:
        return 0
    maxDist = float('-inf')

    seen.add(pt)
    for i in graph[pt]:
        if i not in seen:
            maxDist = max(maxDist, dfs(i) + graph[pt][i])
    seen.remove(pt)

    return maxDist

print(dfs(start))