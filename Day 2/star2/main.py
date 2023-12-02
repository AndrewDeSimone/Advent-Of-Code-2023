import re
data = 'real' #test/real
input = open(f'Day 2\star2\\{data}input.txt', 'r').read().split('\n')

sum = 0

for i in input:
    temp = i.split()
    temp = temp[2:]
    temp = "".join(temp)
    rounds = temp.split(';')
    red = 0
    green = 0
    blue = 0
    for j in rounds:
        for k in j.split(','):
            count = int(re.sub('[^0-9]', '', k))
            color = re.sub('[0-9]', '', k)
            if(color == 'red'): red = max(count, red)
            if(color == 'green'): green = max(count, green)
            if(color == 'blue'): blue = max(count, blue)
    sum += red * green * blue
print(sum) 