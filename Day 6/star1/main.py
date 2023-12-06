import re
import math
data = 'real' #test/real
input = open(f'Day 6\star1\\{data}input.txt', 'r').read().split('\n')

times = re.findall(r'\d+', input[0])
distances = re.findall(r'\d+', input[1])

result = 1

for i in range(0, len(times)):
    value1 = ((int(times[i]) + math.sqrt(int(times[i])**2 - 4 * int(distances[i]))) / 2)+1
    value2 = (int(times[i]) - math.sqrt(int(times[i])**2 - 4 * int(distances[i]))) / 2
    if value1 % 1 == 0:
        value1 -= .1
    if value2 % 1 == 0:
        value2 += .1
    result *= (math.floor(value1)-math.ceil(value2))

print(result)