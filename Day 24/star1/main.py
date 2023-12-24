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
    a1, b1, c1 = stone1.a, stone1.b, stone1.c
    a2, b2, c2 = stone2.a, stone2.b, stone2.c
    if a1*b2 == a2*b1:
       continue
    x = (c1*b2 - c2*b1)/(a1*b2 - a2*b1)
    y = (a2*c1 - a1*c2)/(b1*a2 - a1*b2)
    if testMin <= x <= testMax and testMin <= y <= testMax:
        if (x - stone1.sx) * stone1.vx >= 0 and (y - stone1.sy) * stone1.vy >= 0:
            if (x - stone2.sx) * stone2.vx >= 0 and (y - stone2.sy) * stone2.vy >= 0:\
                count+=1

print(count)