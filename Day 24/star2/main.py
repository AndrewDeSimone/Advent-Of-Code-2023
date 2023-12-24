import sympy
data = 'real' #test/real
input = open(f'Day 24\star2\\{data}input.txt', 'r').read().split('\n')

hailstones = [tuple(map(int, line.replace('@', ',').split(','))) for line in input]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols('xr, yr, zr, vxr, vyr, vzr')

equations = []
answers = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr-sx)*(vy-vyr) - (yr-sy)*((vx-vxr)))
    equations.append((yr-sy)*(vz-vzr) - (zr-sz)*((vy-vyr)))
    if i < 2:
        continue
    answers = [soln for soln in sympy.solve(equations) if all(x%1 == 0 for x in soln.values())]
    if len(answers) == 1:
        break

answer = answers[0]
print(answer[xr] + answer[yr] + answer[zr])