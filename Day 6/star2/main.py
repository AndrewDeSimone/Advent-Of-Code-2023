import re
import math
data = 'real' #test/real
input = open(f'Day 6\star2\\{data}input.txt', 'r').read().split('\n')

time = re.sub(' ', '', input[0].split(':')[1])
distance = re.sub(' ', '', input[1].split(':')[1])

value1 = ((int(time) + math.sqrt(int(time)**2 - 4 * int(distance))) / 2)+1
value2 = (int(time) - math.sqrt(int(time)**2 - 4 * int(distance))) / 2
if value1 % 1 == 0:
    value1 -= .1
if value2 % 1 == 0:
    value2 += .1
print(math.floor(value1)-math.ceil(value2))
    