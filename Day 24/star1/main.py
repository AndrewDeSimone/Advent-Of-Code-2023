import numpy as np
class hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy*sx - vx*sy


data = 'real' #test/real
input = open(f'Day 24\star1\\{data}input.txt', 'r').read().split('\n')
input = [i.replace('@', ',') for i in input]

testSpace = {'test': [7, 27], 'real': [200000000000000, 400000000000000]}
testMin = testSpace[data][0]
testMax = testSpace[data][1]

hailstones = [hailstone(*(map(int, stone.split(',')))) for stone in input]

count = 0

for i, stone1 in enumerate(hailstones):
 for stone2 in hailstones[:i]:
    A = np.array([[stone1.a, stone1.b],[stone2.a, stone2.b]])
    B = np.array([[stone1.c], [stone2.c]])
    if np.linalg.det(A) == 0:
       continue
    x, y = np.dot(np.linalg.inv(A), B).flatten()
    if testMin < x < testMax and testMin < y < testMax:
       if (x - stone1.sx) * stone1.vx >= 0 and (y - stone1.sy) * stone1.vy >= 0:
            if (x - stone2.sx) * stone2.vx >= 0 and (y - stone2.sy) * stone2.vy >= 0:
                count+=1
    

print(count)