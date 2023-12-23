from collections import deque

data = 'real' #test/real
bricks = open(f'Day 22\star2\\{data}input.txt', 'r').read().split('\n')
bricks = [list(map(int, brick.replace('~',',').split(','))) for brick in bricks]
bricks.sort(key=lambda brick: brick[2])

def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for index, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:index]:
        if overlaps(brick, check):
            max_z = max(check[5] + 1, max_z)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

bricks.sort(key = lambda brick: brick[2])

k_supports_v = {i: set() for i in range(len(bricks))}
v_supports_k = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0

for i in range(len(bricks)):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
        j = q.popleft()
        for k in k_supports_v[j] - falling:
            if v_supports_k[k] <= falling:
                q.append(k)
                falling.add(k)
    total+=len(falling)-1

print(total)
